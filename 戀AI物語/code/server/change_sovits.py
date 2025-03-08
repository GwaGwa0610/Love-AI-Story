from gradio_client import Client

client = Client("http://localhost:9872/")
result = client.predict(
		sovits_path="server/SoVITS_weights/D2_e8_s120.pth",
		prompt_language="中文",
		text_language="中文",
		api_name="/change_sovits_weights"
)
print(result)