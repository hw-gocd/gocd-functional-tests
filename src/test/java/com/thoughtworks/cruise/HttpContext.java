package com.thoughtworks.cruise;

import java.io.File;

import org.apache.commons.httpclient.protocol.Protocol;
import org.apache.commons.httpclient.protocol.SecureProtocolSocketFactory;
import org.apache.commons.io.FileUtils;

import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;
import com.thoughtworks.cruise.exceptions.CannotAccessUrlException;
import com.thoughtworks.cruise.ssl.AuthSSLProtocolSocketFactory;
import com.thoughtworks.cruise.ssl.KeyStoreManager;
import com.thoughtworks.cruise.ssl.PermissiveSSLProtocolSocketFactory;
import com.thoughtworks.cruise.state.ScenarioState;

public class HttpContext {

	public static enum ApiTransport {
		HTTP(new Lambda() {
			public void call(ScenarioState scenarioState) {}
		}), 
		HTTPS(new Lambda() {
			public void call(ScenarioState scenarioState) {
				register(new PermissiveSSLProtocolSocketFactory(), scenarioState);
			}
		}), SHINE_LIKE(new Lambda() {
			public void call(ScenarioState scenarioState) {
				FileUtils.deleteQuietly(new File(TWIST_TRUST_JKS));
				register(new AuthSSLProtocolSocketFactory(new File(TWIST_TRUST_JKS), new File(RuntimePath.getServerConfigPath() +"/shine_store.jks") , "Cru153Sh1n3Pa55w0rd",new KeyStoreManager()), scenarioState);
			}
		}), BROWSER(new Lambda() {
			public void call(ScenarioState scenarioState) {	}
		}) {
			@Override
			public byte[] getContentsForPage(String feedUrl, ScenarioState scenarioState) {
				CruiseResponse resp = new TalkToCruise(scenarioState).get(feedUrl);
				return resp.getBody().getBytes();
			}			
		};

		interface Lambda {
			void call(ScenarioState scenarioState);
		}

		private Lambda lambda;

		private ApiTransport(Lambda lambda) {
			this.lambda = lambda;
		}

		private void enable(ScenarioState scenarioState) {
			scenarioState.setApiTransportScheme(this);
			lambda.call(scenarioState);
		}

		private static void register(SecureProtocolSocketFactory factory, ScenarioState scenarioState) {
			Protocol.registerProtocol("https", new Protocol("https", factory, Integer.parseInt(Urls.SSL_PORT)));
		}

		public byte[] getContentsForPage(String feedUrl, ScenarioState scenarioState) {
			TalkToCruise talkToCruise = new TalkToCruise(scenarioState);
			CruiseResponse cruiseResponse = talkToCruise.get(feedUrl);
			if (!cruiseResponse.isSuccess()) {
				throw new CannotAccessUrlException(cruiseResponse);
			}
			return cruiseResponse.getBody().getBytes();
		}
	}

	private static final String TWIST_TRUST_JKS = "twist_trust.jks";
	private ScenarioState scenarioState;

	public HttpContext(ScenarioState scenarioState) {
		this.scenarioState = scenarioState;
	}

	@com.thoughtworks.gauge.Step("Using <scheme>")
	public void using(String scheme) {
		ApiTransport.valueOf(scheme).enable(scenarioState);
	}
}
