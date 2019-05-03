.PHONY : help

KB=192.168.1.101:9901
KB_BASE=/home/hubert/Codes/kb.knoconida.com/

JENKINS=192.168.1.101:9902

MONGODB=192.168.1.101:27017
MONGODB_BASE=/home/hubert/Codes/MongoDB



help : 
	@echo "help commands:"
	@echo "  make run/stop/start/restart/remove KB"
	@echo "  make run/stop/start/restart/remove JENKINS"
	@echo "  make run/stop/start/restart/remove MongoDB"


runMongo :
	@echo "Run MongoDB: "
	cd $(MONGODB_BASE) && sudo docker-compose up -d
	@echo "done......."
	@echo 

stopMongo : 
	@echo "Stop MongoDB: "
	cd $(MONGODB_BASE)  && sudo docker-compose stop
	@echo "done......."
	@echo 

startMongo : 
	@echo "Start MongoDB: "
	cd $(MONGODB_BASE)  && sudo docker-compose start
	@echo "done......."
	@echo 

restartMongo : 
	@echo "Restart MongoDB: "
	cd $(MONGODB_BASE)  && sudo docker-compose restart
	@echo "done......."
	@echo 

removeMongo : 
	@echo "Remove MongoDB: "
	cd $(MONGODB_BASE) && sudo docker-compose down
	@echo "done......."
	@echo 



runKB: 
	@echo "run kb at: $(KB)"
	cd $(KB_BASE) && sudo docker-compose up -d
	@echo "done......"
	@echo
	@echo

stopKB: 
	@echo "stop kb at: $(KB)"
	cd $(KB_BASE) && sudo docker-compose stop
	@echo "done......"
	@echo
	@echo

startKB: 
	@echo "start kb at: $(KB)"
	cd $(KB_BASE) && sudo docker-compose start
	@echo "done......"
	@echo
	@echo

restartKB: 
	@echo "restart kb at: $(KB)"
	cd $(KB_BASE) && sudo docker-compose restart
	@echo "done......"
	@echo
	@echo

removeKB: 
	@echo "remove kb at: $(KB)"
	cd $(KB_BASE) && sudo docker-compose down
	@echo "done......"
	@echo
	@echo

runJenkins: 
	@echo "run Jeknins at: $(JEKINS)"
	sudo docker run --name myJenkins -d -v jenkins_home:/var/jenkins_home -p 9902:8080 -p 50000:50000 jenkins/jenkins:lts
	@echo "done......"
	@echo
	@echo

stopJenkins : 
	@echo "stop Jeknins at: $(JENKINS)"
	sudo docker stop myJenkins
	@echo "done......"
	@echo
	@echo

startJenkins : 
	@echo "start Jeknins at: $(JENKINS)"
	sudo docker start myJenkins 
	@echo "done......"
	@echo
	@echo

restartJenkins : 
	@echo "stop Jeknins at: $(JENKINS)"
	sudo docker restart myJenkins 
	@echo "done......"
	@echo
	@echo

removeJenkins : 
	@echo "remove Jeknins at: $(JENKINS)"
	sudo docker rm myJenkins 
	@echo "done......"
	@echo
	@echo


