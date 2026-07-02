meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
minimas = [19, 19, 19, 17, 14, 13, 12, 13, 14, 16, 17, 18]
maximas = [27, 28, 27, 25, 23, 22, 22, 23, 24, 25, 26, 26]
medias = [(minima + maxima) / 2 for minima, maxima in zip(minimas, maximas)]
media_meses = [f"{mes} | {media}" for mes, media in zip(meses, medias)]

for i in media_meses:
    print(i)


def response(hey_bob):
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = any(c.isalpha() for c in hey_bob) and hey_bob == hey_bob.upper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"

    if is_yelling:
        return "Whoa, chill out!"

    if is_question:
        return "Sure."

    return "Whatever."

while True:
    N = input()
    if N == "0":
        break
    print(response(N))