package com.thoughtworks.cruise;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.api.UsingPipelineApi;
import com.thoughtworks.cruise.page.OnPipelineDashboardPage;

public class PipelineVisibility {

    private String pipelineName;

    private final OnPipelineDashboardPage dashboardPage;

    private final UsingPipelineApi usingPipelineApi;

    public PipelineVisibility(Browser browser, OnPipelineDashboardPage dashboardPage, UsingPipelineApi usingPipelineApi) {
        this.dashboardPage = dashboardPage;
        this.usingPipelineApi = usingPipelineApi;
    }

    public void setPipelineName(String pipelineName) throws Exception {
        this.pipelineName = pipelineName;
        dashboardPage.lookingAtPipeline(pipelineName);
        usingPipelineApi.forPipeline(pipelineName);
    }

    public void setUp() throws Exception {
        dashboardPage.open();
    }

    public void tearDown() throws Exception {
        dashboardPage.open();
    }

    public String isVisible() throws Exception {
        try {
            dashboardPage.verifyPipelineIsVisible(pipelineName);
        } catch (AssertionError failure) {
            return "false";
        }
        return "true";
    }

    public String canOperate() throws Exception {
        try {
            usingPipelineApi.scheduleShouldReturnCode(202);
        } catch (AssertionError failure) {
            return "false";
        } catch (RuntimeException e) {
            return "false";
        }
        return "true";
    }
    
public String canOperateUsingUi() throws Exception{
        
        try {
			dashboardPage.verifyTriggerButtonIsPresent();
			dashboardPage.verifyTriggerWithOptionsButtonIsPresent();
		} catch (AssertionError failure) {			
			return "false";
		} catch (Exception e) {			
			return "false";
		}
        return "true";

    }

    public String canPauseUsingApi() throws Exception{
        try {
            usingPipelineApi.attemptToPausePiplineWithCauseAndShouldReturnWithHttpStatus(pipelineName,"Pausing",200);
            usingPipelineApi.attemptToUnpausePipelineAndShouldReturnWithHttpStatus(pipelineName, 200);
        } catch (AssertionError failure) {
            return "false";
        } catch (Exception e) {
            return "false";
        }
        return "true";
    }

    public String canPauseUsingUi() throws Exception {
        
        try {
			dashboardPage.pausePipelineWithReason("Pausing through UI");
			dashboardPage.verifyPipelineIsPausedWithReason("Pausing through UI");
			dashboardPage.unpausePipeline();
			dashboardPage.verifyPipelineIsUnpaused();
		} catch (AssertionError failure) {			
			return "false";
		} catch (Exception e) {			
			return "false";
		}
        return "true";
    }

	@com.thoughtworks.gauge.Step("PipelineVisibility <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Exception {
		com.thoughtworks.twist.migration.brt.BRTMigrator.BRTExecutor(table, this);
	
	}

}
