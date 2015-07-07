package com.thoughtworks.cruise.client;

import java.io.File;
import java.io.IOException;
import java.util.List;

import org.apache.commons.httpclient.Header;
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.HttpException;
import org.apache.commons.httpclient.HttpMethodBase;
import org.apache.commons.httpclient.HttpStatus;
import org.apache.commons.httpclient.NameValuePair;
import org.apache.commons.httpclient.URI;
import org.apache.commons.httpclient.UsernamePasswordCredentials;
import org.apache.commons.httpclient.auth.AuthScope;
import org.apache.commons.httpclient.methods.DeleteMethod;
import org.apache.commons.httpclient.methods.EntityEnclosingMethod;
import org.apache.commons.httpclient.methods.GetMethod;
import org.apache.commons.httpclient.methods.PostMethod;
import org.apache.commons.httpclient.methods.PutMethod;
import org.apache.commons.httpclient.methods.RequestEntity;
import org.apache.commons.httpclient.methods.multipart.FilePart;
import org.apache.commons.httpclient.methods.multipart.MultipartRequestEntity;
import org.apache.commons.httpclient.methods.multipart.Part;
import org.apache.commons.httpclient.methods.multipart.StringPart;

import com.thoughtworks.cruise.state.CurrentUsernameProvider;

public class TalkToCruise {
	
	private final CurrentUsernameProvider currentUserNameProvider;
	
	public TalkToCruise(CurrentUsernameProvider state) {
		this.currentUserNameProvider = state;
	}

	public CruiseResponse post(String url, List<NameValuePair> nameValuePairs) {
		return post(url, toArray(nameValuePairs));
	}

	public CruiseResponse post(String url, NameValuePair... nameValuePairs) {
		HttpClient client = client();
		PostMethod post = new PostMethod(url);
		post.addParameters(nameValuePairs);
		return execute(url, client, post);
	}

	private CruiseResponse execute(String url, HttpClient client, EntityEnclosingMethod post) {
		try {
			client.executeMethod(post);
			CruiseResponse response = new CruiseResponse(post);					
			return response;
		} catch (IOException e) {
			throw new RuntimeException("Error while trying to POST to url " + url + ".", e);
		}
	}

	public CruiseResponse post(String url, File file, String partName) throws HttpException, IOException {
		HttpClient client = client();
		PostMethod filePost = new PostMethod(url);
		filePost.setRequestEntity(new MultipartRequestEntity(new Part[]{new FilePart(partName, file)}, filePost.getParams()));
		return execute(url, client, filePost);
	}

	public CruiseResponse put(String url, String text, String partName) {
		HttpClient client = client();
		PutMethod put = new PutMethod(url);
		put.setRequestEntity(new MultipartRequestEntity(new Part[]{new StringPart(partName, text)}, put.getParams()));
		return execute(url, client, put);
	}

	public CruiseResponse put(String url, RequestEntity reqEntity) {
		HttpClient client = client();
		PutMethod put = new PutMethod(url);
		put.setRequestEntity(reqEntity);
		return execute(url, client, put);
	}

	public CruiseResponse get(String url, List<NameValuePair> nameValuePairs) {
		return get(url, toArray(nameValuePairs));
	}

	public CruiseResponse get(String url, NameValuePair... nameValuePairs) {
		return get(url, true, nameValuePairs);
	}
	
	public CruiseResponse get(String url, boolean shouldFollowRedirect, NameValuePair... nameValuePairs) {
		GetMethod get = new GetMethod(url);
		get.setQueryString(nameValuePairs);
		get.setFollowRedirects(shouldFollowRedirect);
		return execute(url, get, true);
	}
	
	public CruiseResponse delete(String url) {
        DeleteMethod del = new DeleteMethod(url);
        return execute(url, del, true);
    }

	public CruiseResponse getWithoutBasicAuth(String url, String headerName, String headerValue) {
		GetMethod get = new GetMethod(url);
		get.addRequestHeader(headerName, headerValue);
		return execute(url, get, false);
	}
	
	private CruiseResponse execute(String url, HttpMethodBase method, boolean useBasicAuth) {
		try {
			client(useBasicAuth).executeMethod(method);
			return new CruiseResponse(method);
		} catch (IOException e) {
			throw new RuntimeException("Error while trying to GET url " + url + ".", e);
		}
	}

	public static class CruiseResponse {
		private final int status;
		private final String body;
		private URI uri;
		private final HttpMethodBase method;

		public CruiseResponse(HttpMethodBase method) {
			this.method = method;
			this.status = method.getStatusCode();
			try {
				this.body = method.getResponseBodyAsString();
				this.uri = method.getURI();
			} catch (IOException e) {
				throw new RuntimeException(e);
			}			
		}
		
		public int getStatus() {
			return status;
		}
		
		public String getBody() {
			return body;
		}
		
		public boolean isSuccess() {
			return (status >= 200 && status < 400);	
		}

		public boolean isForbidden() {
			return status == HttpStatus.SC_FORBIDDEN;	
		}

		@Override
		public String toString() {
			return String.format("Response-> status: %s | body: %s ------ Request-> url: %s ", status, body, uri);
		}
		
		public String getResponseHeader(String header) {
			Header responseHeader = method.getResponseHeader(header);
            return responseHeader == null ? null : responseHeader.getValue();
		}
	}

	private NameValuePair[] toArray(List<NameValuePair> nameValuePairs) {
		return nameValuePairs.toArray(new NameValuePair[nameValuePairs.size()]);
	}

	private HttpClient client() {
		return client(true);
	}

	private HttpClient client(boolean shouldUseBasicAuth) {
		HttpClient httpClient = new HttpClient();
		String userName = currentUserNameProvider.loggedInUser();
		if (userName != null && shouldUseBasicAuth) {
			httpClient.getParams().setAuthenticationPreemptive(true);
            httpClient.getState().setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(userName, "badger"));
		}
		return httpClient;
	}
}
