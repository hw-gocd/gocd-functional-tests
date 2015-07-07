package com.thoughtworks.cruise.state;

import java.util.HashMap;
import java.util.Map;

public class OauthState {

	private Map<String, OauthClient> oauthClients = new HashMap<String, OauthClient>();
	
	public static class OauthClient {
		private String id;
		private String secret;
		private final String redirectURI;
		private String authCode;
		private Map<String, String> userNameToToken = new HashMap<String, String>();
		
		public OauthClient(String id, String secret, String redirectURI) {
			this.id = id;
			this.secret = secret;
			this.redirectURI = redirectURI;
		}
		
		public String getId() {
			return id;
		}
		
		public String getSecret() {
			return secret;
		}
		
		public String getRedirectURI() {
			return redirectURI;
		}

		public void setAuthCode(String authCode) {
			this.authCode = authCode;
		}

		public String getAuthCode() {
			return authCode;
		}

		public void setAccessTokenForUser(String username, String accessToken) {
			userNameToToken.put(username, accessToken);
		}

		public String getAccessToken(String username) {
			return userNameToToken.get(username);
		}
	}
	
	public void saveOauthClient(String name, OauthClient client) {
		oauthClients.remove(name);
		oauthClients.put(name, client);
	}
	
	public OauthClient getOauthClientNamed(String name) {
		return oauthClients.get(name);
	}
}
