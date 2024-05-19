from simplegmail import Gmail

gmail = Gmail() # will open a browser window to ask you to log in and authenticate

params = {
  "to": "tiago.magalhaes@aluno.uece.br",
  "sender": "tiago.magalhaes@aluno.uece.br",
  "subject": "My first email",
  "msg_html": "<h1>Woah, my first email!</h1><br />This is an HTML email.",
  "msg_plain": "Hi\nVSF.",
  "signature": True  
}
message = gmail.send_message(**params)  