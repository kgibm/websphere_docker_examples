nodeName = AdminControl.getNode()
serverName = AdminServerManagement.listServers()[0]
serverName = serverName[:serverName.find("(")]
AdminApplication.uninstallApplication("DefaultApplication")
# https://www.ibm.com/support/knowledgecenter/en/SSAW57_9.0.0/com.ibm.websphere.nd.multiplatform.doc/ae/rxml_taskoptions.html
AdminApp.install("/work/java_hello_world.ear", ["-appname", "java_hello_world", "-node", nodeName, "-server", serverName, "-usedefaultbindings"])
AdminConfig.save()
