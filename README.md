# mailnews
The latest news from the world's leading press in telegram

The bot reads news from the leading American, French, English press, translates headlines and descriptions into Russian, and checks for the presence of keywords of interest in this news. If there is news, it publishes it in a private message telegram, in Russian with links. Publishes up to 5 found news. When restarted, deletes the previous message and creates a new one. Recommended for daily use.

1. Edit the .env file: TELEGRAM_TOKEN, CHAT_ID, and KEYWORDS in the same way, adding the roots of the words you are interested in,
2. Make sure that the bot can write to you by writing a message to the bot,
3. Make sure that all the urls listed in .env (RSS_UK variable) are accessible from the server,
4. Check that all the necessary libraries are installed: telebot, python-dotenv, asyncio, googletrans, feedparser,
5. Run the bot once a day, for example, in the morning. This can be done via crontab: 40 7 * * * /usr/local/bin/python3 /usr/home/test/main.py (of course, it is advisable to use a virtual environment). After publishing the next summary, the previous message will be deleted.

# Новости прессы
Самые свежие новости от ведущей мировой прессы в телеграмме

Бот читает новости ведущей американской, французской, английской прессы, переводит заголовки и описания на русский, и проверяет нахождение интересующих ключевых слов в этих новостях. Если новости есть, он публикует их в личном сообщении телеграмма, на русском языке со ссылками. Публикует до 5 найденных новостей. При повторном запуске удаляет предыдущее сообщение и создаёт новое. Рекомендуется для ежедневного использования.

1. Отредактируйте файл .env: TELEGRAM_TOKEN, CHAT_ID, а также KEYWORDS по подобию, внеся корни интересующих Вас слов,
2. Убедитесь, что бот может писать Вам, написав сообщение боту,
3. Убедитесь, что с сервера доступны все url, перечисленные в .env (переменная RSS_UK),
4. Проверьте, что установлены все необходимые библиотеки: telebot, python-dotenv, asyncio, googletrans, feedparser,
5. Запускайте бота раз в сутки, например, по утрам. Это возможно сделать через crontab: 40 7 * * * /usr/local/bin/python3 /usr/home/test/main.py (разумеется, желательно использовать виртуальное окружение). После публикации очередной сводки предыдущее сообщение будет удалено.
