Vorher0 = {
    0: [[0, 0, 0, 0], [0, 0, 2, 0]],
    60: [[0, 0, 2, 0]],
    90: [[0, 0, 0, 0], [2, 0, 0, 0], [1, 0, 2, 1]],
    120: [[2, 0, 2, 0]],
}
Nachher0 = {
    0: [],
    60: [[0, 0, 0, 0], [0, 0, 2, 0]],
    90: [[0, 0, 0, 0], [2, 0, 0, 0], [1, 0, 0, 1]],
    120: [[2, 0, 0, 0], [2, 0, 2, 0]],
}
Vorher1 = {
    30: [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, 1, 0]],
    90: [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, 1, 0]],
    150: [[0, 1, 1, 0], [0, 2, 2, 0], [0, 1, 3, 0]],
}
Nachher1 = {
    30: [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, -1, 0]],
    90: [[0, 0, 0, 0], [0, 2, 0, 0], [0, 1, 1, 0]],
    150: [[0, 2, 2, 0], [0, 2, 0, 0], [0, 1, -1, 0]],
}
Vorher2 = {
    0: [[1, 0, 0, 1], [3, 0, 0, 1], [1, 0, 2, 1], [3, 0, 2, 1]],
    30: [[1, -1, 1, 1], [5, 0, 0, 1]],
    60: [[0, 0, 0, 0], [4, 0, 0, 0]],
    90: [[1, 0, 0, 1], [5, 0, 0, 1]],
    120: [[2, 0, 0, 0], [6, 0, 0, 0], [5, 0, 2, 1]],
    150: [[5, 1, 1, 1]],
}
Nachher2 = {
    0: [[1, 0, 0, 1], [3, 0, 0, 1], [1, 0, 2, 1], [3, 0, 2, 1]],
    30: [[5, -1, 1, 1]],
    60: [[0, 0, 0, 0], [4, 0, 0, 0]],
    90: [[1, 0, 0, 1], [5, 0, 0, 1]],
    120: [[2, 0, 0, 0], [6, 0, 0, 0], [5, 0, 2, 1]],
    150: [[5, 0, 0, 1], [1, 0, 2, 1]],
}
Vorher3 = {
    30: [[0, 0, 0, 0], [0, 1, -1, 0], [0, 2, 0, 0], [0, 3, -1, 0]],
    60: [[0, 2, 0, 0], [-1, 2, 0, 1], [-1, 2, 0, -1], [0, 2, 0, -2]],
    120: [[0, 2, 0, 0], [1, 2, 0, 1], [1, 2, 0, -1], [0, 2, 0, -2]],
    150: [[0, 1, -1, 0], [0, 2, 0, 0], [0, 3, -1, 0], [0, 4, 0, 0]],
}
Nachher3 = {
    0: [[2, 0, 0, 2], [0, 0, 0, 2]],
    30: [[2, 0, 0, 2], [2, -1, -1, 2]],
    60: [[0, 0, 0, 0], [1, 0, 0, 1], [2, 0, 0, 2]],
    90: [[2, 0, 0, 2], [2, 0, -2, 2], [2, 0, -4, 2], [2, 0, 2, 2]],
    120: [[2, 0, 0, 2], [4, 0, 0, 0], [3, 0, 0, 1]],
    150: [[2, 0, 0, 2], [2, 1, -1, 2]],
}
Vorher4 = {
    0: [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [6, 0, 0, 0],
        [0, 0, 2, 0],
        [2, 0, 2, 0],
        [4, 0, 2, 0],
        [4, 0, -2, 0],
        [6, 0, -2, 0],
    ],
    90: [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [6, 0, 0, 0],
        [4, 0, -2, 0],
        [6, 0, -2, 0],
        [8, 0, -2, 0],
    ],
}
Nachher4 = {
    0: [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [6, 0, 0, 0],
        [0, 0, 2, 0],
        [4, 0, 2, 0],
        [2, 0, -2, 0],
        [6, 0, -2, 0],
    ],
    90: [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [6, 0, 0, 0],
        [2, 0, -2, 0],
        [4, 0, -2, 0],
        [6, 0, -2, 0],
        [8, 0, -2, 0],
    ],
}
Vorher5 = {
    30: [[0, 0, 0, 0], [0, 1, 1, 0], [0, 2, 2, 0]],
    90: [[0, 1, -1, 0], [0, 1, 1, 0], [0, 1, 3, 0]],
    150: [[0, 1, 3, 0], [0, 2, 2, 0], [0, 3, 1, 0]],
}
Nachher5 = {
    30: [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, 1, 0]],
    90: [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, 1, 0]],
    150: [[0, 1, 1, 0], [0, 2, 2, 0], [0, 1, 3, 0]],
}

import sys

# Vorher ist die Streichholzanordnung,
# die in die Streichholzanordnung Nachher ??berf??hrt werden soll
# Beide Streichholzanordnungen m??ssen gleich lang sein
# u ist die Anzahl der Streichh??lzer, die umgelegt werden sollen
if len(sys.argv) < 4:
    # Wenn nicht genug Parameter angegeben wurden,
    # wird eine L??sung des ersten Beispiels ausgegeben
    print(
        "Nicht genug Parameter wurden angegeben, hier ist eine L??sung des ersten Beispiels"
    )
    Vorher = Vorher0
    Nachher = Nachher0
    u = 3
else:
    Vorher = sys.argv[1]
    Nachher = sys.argv[2]
    u = sys.argv[3]
    exec("Vorher = " + Vorher)
    exec("Nachher = " + Nachher)
    exec("u = " + u)
# n ist die Anzahl der Streichh??lzer in Vorher/Nachher
n = sum([len(v) for v in Vorher.values()])


# Implementierung von Subtraktion von Punkten/Vektoren
def vektorMinus(vektor1, vektor2):
    return [vektor1[index] - vektor2[index] for index in range(0, 4)]


def ??bereinanderlegen(Vektor):
    def ausgeben(UmzulegendVorher, UmzulegendNachher):
        if u == umzulegend + 1:
            # Wenn es ein umzulegendes Streichholz weniger gibt als u,
            # Wird ein passendes Streichholz statt einem umzulegenden umgelegt
            UmzulegendVorher[passendesStreichholz[1]] += [passendesStreichholz[0]]
            UmzulegendVorher[umzulegendesStreichholz[1]].remove(
                umzulegendesStreichholz[0]
            )
        # UmzulegendVorher und UmzulegendNachher werden gek??rzt
        UmzulegendVorher = {k: v for (k, v) in UmzulegendVorher.items() if len(v) > 0}
        UmzulegendNachher = {k: v for (k, v) in UmzulegendNachher.items() if len(v) > 0}
        # Die umzulegenden Streichh??lzer von Vorher werden auf die von Nachher gelegt
        L??sung = f"Das R??tsel ist l??sbar.\nDie {umzulegend} Streichh??lzer an folgenden Positionen:\n{UmzulegendVorher}\nwerden an diese Positionen verschoben und gedreht\n{UmzulegendNachher}."
        # Die L??sung wird erg??nzt, wenn es weniger umzulegende Streichh??lzer gibt als u
        if u == umzulegend + 1:
            # Wenn es ein umzulegendes Streichholz weniger gibt als u,
            # Wird das umzulegende Streichholz auf den ehemaligen Platz des passenden gelegt
            L??sung += f"\n{umzulegendesStreichholz} wird an diese Positionen verschoben und gedreht {passendesStreichholz}."
        elif u >= umzulegend + 2:
            # Wenn es noch weniger umzulegende Streichh??lzer gibt,
            # werden die fehlenden miteinander getauscht
            L??sung += f"\n{u - umzulegend} andere Streichh??lzer tauschen gegenseitig ihre Pl??tze."
        # Der L??sungssatz L??sung wird zur??ckgegeben
        return L??sung

    # Jedes Streichholz von Nachher wird um den Vektor verschoben
    # UmzulegendNachher speichert umzulegende Streichh??lzer von Nachher
    # UmzulegendVorher speichert umzulegende Streichh??lzer von Vorher
    UmzulegendNachher = {
        k: [vektorMinus(i, Vektor) for i in v] for (k, v) in Nachher.items()
    }
    UmzulegendVorher = {0: [], 30: [], 60: [], 90: [], 120: [], 150: []}
    # Mit umzulegend werden die umzulegenden Streichh??lzer gez??hlt,
    umzulegend = 0
    for Winkel in Vorher:
        for Vorherpunkt in Vorher[Winkel]:
            if Vorherpunkt in UmzulegendNachher[Winkel]:
                # Wenn ein Streichholz passend ist, wird es aus UmzulegendNachher gel??scht,
                # damit am Ende die umzulegenden Streichh??lzer ??brig bleiben
                UmzulegendNachher[Winkel].remove(Vorherpunkt)
                # passendesStreichholz ist ein passendes Streichholz von Vorher
                passendesStreichholz = [Vorherpunkt, Winkel]
            else:
                # Wenn nicht, wird UmzulegendVorher das Streichholz hinzugef??gt
                UmzulegendVorher[Winkel] += [Vorherpunkt]
                umzulegend += 1
                # umzulegendesStreichholz ist ein umzulegendesStreichholz von Vorher
                umzulegendesStreichholz = [Vorherpunkt, Winkel]
        if umzulegend > u:
            # Falls es mehr umzulegende Streichh??lzer gibt als u, wird die Funktion abgebrochen
            return None
    # Wenn genau u Streichh??lzer umgelegt werden m??ssen, wird die L??sung zur??ckgegeben
    return ausgeben(UmzulegendVorher, UmzulegendNachher)


def streichholzr??tsel():
    if u == n:
        # Wenn u und n gleich sind, wird jeder Vektor eine L??sung zur??ckgeben
        return ??bereinanderlegen([0, 0, 0, 0])
    # Vektoren speichert alle Vektoren
    Vektoren = []
    # Alle Vektoren, bei denen es mindestens 1 umzulegendes Streichholz gibt, werden erstellt
    for Winkel in Vorher:
        for Vorherpunkt in Vorher[Winkel]:
            for Nachherpunkt in Nachher[Winkel]:
                Vektor = vektorMinus(Nachherpunkt, Vorherpunkt)
                # Wenn der Vektor noch nicht getestet wurde,
                # bestimmt die Vergleichsfunktion, ob der Vektor der richtige Vektor ist
                if Vektor not in Vektoren:
                    Vektoren += [Vektor]
                    Ergebnis = ??bereinanderlegen(Vektor)
                    if Ergebnis:
                        # Wenn eine L??sung gefunden wurde, wird diese zur??ckgegeben
                        return Ergebnis
    # Wenn keine L??sung gefunden wurde, ist das R??tsel nicht l??sbar
    return "Das R??tsel ist nicht l??sbar"


print(streichholzr??tsel())