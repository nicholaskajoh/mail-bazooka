# Mail Bazooka

Simple python script to send an email to a large number of addresses using Mailgun's email API.

## Example

**FORMAT:** `python main.py [MAILGUN-API-BASE-URL] [MAILGUN-API-KEY] [FROM-EMAIL] [T0-EMAIL-LIST] [EMAIL-SUBJECT] [EMAIL-BODY]`

**SAMPLE:** `python main.py "https://api.mailgun.net/v3/samples.mailgun.org/messages" "key-3ax6xnjp29jd6fds4gc373sgvjxteol0" "Vandal Savage <vandalis@savage.io>" "email_list.example.txt" "I'm Savage" "email_body.example.txt"`

**NB: You must be connected to the internet to consume the API.**

## Dependencies

* requests (run `pip install requests`)

## License

MIT
