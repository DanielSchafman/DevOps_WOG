import json

class Score:
    def adding_player_score(self, name, difficulty):
        with open('Score.json', 'r') as f:
            data = json.load(f)

        new_score = (difficulty * 3) + 5

        for player in data['players']:
            if player["name"] == name:
                player["score"] += new_score
                break
        else:
            new_player = {
                "name": name,
                "score": new_score
            }
            data['players'].append(new_player)

        with open('Score.json', 'w') as f:
            json.dump(data, f, indent=4)