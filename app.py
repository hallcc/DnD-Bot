

def process_message(message):
    return message.lower()

if __name__ == '__main__':


    index = 0
    groups = groupy.Group.list()
    for i in range(len(groups)):
        print(i)
        if str(groups[i]).split()[0] == 'testing,':
            index = i
            break
    group = groups[index]

    members = group.members()[0:20]

    index = 0
    bots = groupy.Bot.list()
    try:
        for i in range(len(bots)):
            if bots[i] == 'Dungeon Master':
                index = i
        bot = bots[index]
    except:
        bot = groupy.Bot.create('Dungeon Master', group)
        bot.post("Are you ready to meet your fate?")

