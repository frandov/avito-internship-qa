import json
import slack

class SlackSender:
    '''Sender для Slack'''

    def __init__(self):
        try:
            with open('slack_data.json') as f:
                self._json_data = json.load(f)
            self._client = slack.WebClient(token=self._json_data['bot_token'])
        except Exception as e:
            print(f'Exception while get token and parse json: {e}')

    def send_message(self, channel: str, message: str):
        """
        Отправляет сообщение в канал
        """
        try:
            args = {'channel': channel, 'text': message, 'as_user': True, 'link_names': 1}
            res = self._client.chat_postMessage(**args)
        except Exception as e:
            print(f'Exception while sending message: {e}')
            return False
        return res
    
    def send_from_json(self):
        """
        Отправвляет сообщение из json
        """
        try:
            for channel_data in self._json_data['channels']:
                self.send_message(channel_data['channel'], channel_data['text'])
                print(f"Send to {channel_data['channel']}")
        except Exception as e:
            print(f'Exception while sending from json: {e}')
            return False
        return

print('Start!')
SlackSender().send_from_json()
print('Finish!')

# Links To Channels:
# https://join.slack.com/share/zt-v9e72lgw-dgRP3JGVfh0R01Udzz5cIQ
# https://join.slack.com/share/zt-uymsspoz-0fdAIu6UL~ApkPssFdVgzg
# https://join.slack.com/share/zt-uymsspoz-0fdAIu6UL~ApkPssFdVgzg
