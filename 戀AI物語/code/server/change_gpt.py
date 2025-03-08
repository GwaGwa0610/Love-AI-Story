from gradio_client import Client

client = Client("http://localhost:9872/")
result = client.predict(
		weights_path="server/GPT_weights/D2-e15.ckpt",
		api_name="/init_t2s_weights"
)
print(result)
