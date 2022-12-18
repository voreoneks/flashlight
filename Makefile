run:
	docker run -i -p 8000:8000 --env--file ./env/.env.pred -v logs:/usr/local/flashlight/data --name flashlight_con flashlight:latest
start:
	docker start flashlight_con
stop:
	docker stop flashlight_con