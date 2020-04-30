import jenkins

# _jenkins_url='http://localhost:9000'
# _jenkins_user='houzw'
# _jenkins_pwd='houzw'


# get server
server = jenkins.Jenkins(_jenkins_url, username=_jenkins_user, password=_jenkins_pwd)

# get job
jobname = server.get_job_name(name='simple_jobCompose')

jobparams={
    'gitl_branch': 'dev_rpc',
    'compose_jobs': '{"level1":["composeJob_1_1","composeJob_1_2"],"level2":["composeJob_2_1"],"level3":["composeJob_3_1","composeJob_3_2"]}'
}

server.build_job(jobname,jobparams)

build_job_url = server.build_job_url(jobname, jobparams)
print(build_job_url)

last_build_number = server.get_job_info(jobname)['lastCompletedBuild']['number']
build_info = server.get_build_info(jobname, last_build_number)
print(build_info)



# compose_v1.0
# print(jobs)


