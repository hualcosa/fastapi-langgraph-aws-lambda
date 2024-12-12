all: prep package_model synth deploy

prep:
	bash -e scripts/setup.sh

update_notice:
	bash -e scripts/update_notice.sh

package_model:
	. .venv/bin/activate && cd ./chatbot_api/runtime/serving_api && tar czvf ../../docker/serving_api.tar.gz custom_lambda_utils requirements.txt serving_api.py

cdk_bootstrap:
	. ./.venv/bin/activate && cdk bootstrap

synth:
	. .venv/bin/activate && cdk synth

deploy:
	. .venv/bin/activate && cdk deploy

destroy:
	. .venv/bin/activate && cdk destroy

clean: 
	rm -r .venv/ cdk.out/

docker-build:
	docker compose build

docker-run:
	docker compose up

docker-test:
	curl -X POST http://localhost:8000/chat \
		-H "Content-Type: application/json" \
		-d '{"message": "Hello", "session_id": "test-1"}'
