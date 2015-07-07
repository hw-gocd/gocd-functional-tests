package com.thoughtworks.cruise.context;

import java.util.HashMap;
import java.util.Map;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.RuntimePath;
import com.thoughtworks.cruise.preconditions.ProcessIsRunning;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

public class GadgetRenderingServerIsRunning {

	private Browser browser;
	private GadgetRenderingServer gadgetRenderingServer;

	public GadgetRenderingServerIsRunning(Browser browser) {
		this.browser = browser;
	}

	@com.thoughtworks.gauge.Step("Gadget rendering server is running - setup")
	public void setUp() throws Exception {
		gadgetRenderingServer = new GadgetRenderingServer();
		gadgetRenderingServer.start();
	}

	@com.thoughtworks.gauge.Step("Gadget rendering server is running - teardown")
	public void tearDown() throws Exception {
		gadgetRenderingServer.stop();
	}
	
	private static class GadgetRenderingServer extends ProcessIsRunning {

		@Override
		protected boolean pumpOutputStream() {
			return true;
		}

		@Override
		protected boolean pumpErrorStream() {
			return true;
		}

		@Override
		protected boolean isProcessStopped() {
			try {
				return !isServerRunning();
			} catch (RuntimeException e) {
				return true;
			}
		}

		private boolean isServerRunning() {
			return get("http://localhost:3000").getReturnCode() < 400;
		}

		@Override
		protected String startCommand() {
			return "./start_server.sh";
		}

		@Override
		protected String stopCommand() {
			return "./stop_server.sh";
		}

		@Override
		protected String getWorkingDir() {
			return RuntimePath.pathFor("gadget_renderer");
		}

		@Override
		protected Map<String, String> getStartEnvVariables() {
			return new HashMap<String, String>();
		}
		
		@Override
		public void start() throws Exception {
			stop();
			waitTillServerIsStopped();
			execute("./db_reset.sh", new HashMap<String, String>());
			super.start();
			waitTillServerIsStarted();
			System.out.println("Gadget server started");
		}
		
		private void waitTillServerIsStopped() {
			Assertions.waitUntil(Timeout.TWO_MINUTES, new Predicate() {
				public boolean call() throws Exception {
					return isProcessStopped();
				}
			});
		}

		private void waitTillServerIsStarted() {
			Assertions.waitUntil(Timeout.TWO_MINUTES, new Predicate() {
				public boolean call() throws Exception {
					return !isProcessStopped();
				}
			});
		}
	}
}
