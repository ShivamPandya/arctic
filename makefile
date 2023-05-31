state?=idling

archive:
	@python write.py $(state)
	@echo "An $(state) archive has been created!"

tar: 
	@python tar.py

upload:
	@curl -vvvv -F "upload=@./ros-aws-idling.tar.gz;type=application/vnd.redhat.advisor.collection+tgz"  https://console.stage.redhat.com/api/ingress/v1/upload -u insights-qa  | python -m json.tool

help:
	@echo -e "\n+------------------------+\n|   Welcome to Arctic!   |\n+------------------------+"
	@echo -e "Use the following command to create archives:\n \033[43mmake archive state={state_value}\n\033[0mValid state values: optimized, idling, undersized, under-pressure\n"
