# WGSS
D:0.0.1 Weekly Group Summary Service



### POST http://129.168.1.112:9595/api/message/

#Example && #Response
`{
	"chat_id": 84032,
	"message_id": 4324,
  "message_text": "#Some #Text",
  "reply_to_message": 3245
}`

### GET http://129.168.1.112:9595/api/report/<chat_id>/

#Example
  http://129.168.1.112:9595/api/report/1/
  
#Response

`{
	"message_id": 4324,
  "message_text": "#Some #Text",
  "importance": "#Some #Text"
}`
