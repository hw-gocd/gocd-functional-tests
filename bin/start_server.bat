setlocal

set MANUAL_SETTING=Y
set PRODUCTION_MODE=N
set JVM_DEBUG=Y
set GO_SERVER_PORT=8253
set GO_SERVER_SSL_PORT=8254
set GO_SERVER_SYSTEM_PROPERTIES="-Dalways.reload.config.file=true -Dcruise.unresponsive.job.warning=1 -Dcruise.buildCause.producer.interval=10000 -Dcruise.xmpp.port=61221 -Dcruise.pipelineStatus.cache.interval=800 -Dcruise.shine.stage.feed=http://localhost:$GO_SERVER_PORT/cruise/api/feeds/stages.xml -Dcruise.shine.sparql.url=http://localhost:8253/cruise/shine/sparql.xml"

cd ..\..\target\go-server*

REM rmdir /S /Q db
REM rmdir /S /Q config

start-server.bat

tail -f go-server.log

endlocal
