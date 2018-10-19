import groovy.json.JsonSlurper

def json_file = new File("/var/lib/jenkins/jobs/$currentProject.name/workspace/config/blades_special.json")
def config = new JsonSlurper().parseText(json_file.text)
def result = ["ALL"]
config["bp_testcases"].each {result.add(it["report_name"])}
return result