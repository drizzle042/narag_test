import os
from datetime import datetime
from django.conf import settings


def date_converter(date: str) -> str:
	date = date.removesuffix("Z")
	date = datetime.fromisoformat(date)
	date = date.date()
	return date

def handle_file_upload(uploaded_file, uploadDIR: str, filename: str):

	fileDIR = os.path.join(settings.BASE_DIR, "files", uploadDIR)

	if not os.path.exists(fileDIR):
		os.makedirs(fileDIR)

	temp_file = os.path.join(fileDIR, filename)

	with open(temp_file, "wb+") as file:
		for chunk in uploaded_file.chunks():
			file.write(chunk)
	return file
