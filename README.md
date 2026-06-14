# Teorie grafů

Dva programy vzniklé jako součást maturitní práce z informatiky na téma *Grafové aplikace*.

## nim.py – Hra Nim

Interaktivní aplikace, kde hráč hraje proti počítači hru Nim (tahání sirek).
Hráč vybírá hromádku a počet sirek, které chce vytáhnout. Aplikace poskytuje nápovědu,
která vede k výhře. Vítěz je ten, kdo vytáhne poslední sirku.

Nápověda funguje na principu hledání jádra grafu.

## floyd_warshall.py – Floyd-Warshallův algoritmus

Grafový algoritmus pro hledání nejkratší cesty mezi městy. Program má předem daná města
a některé vzdálenosti – ostatní vypočítá algoritmus, případně upraví již zadané hodnoty.
