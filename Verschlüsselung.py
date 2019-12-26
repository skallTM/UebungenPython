# -*- coding: utf-8 -*-
string = "my home is my castle"
string = "auch gibt es niemanden der den schmerz an sich liebt sucht oder wuenscht nur weil er schmerz ist es sei denn es kommt zu zufaelligen umstaenden in denen muehen und schmerz ihm grosse freude bereiten koennen um ein triviales beispiel zu nehmen wer von uns unterzieht sich je anstrengender koerperlicher betaetigung ausser um vorteile daraus zu ziehen aber wer hat irgend ein recht einen menschen zu tadeln der die entscheidung trifft eine freude zu geniessen die keine unangenehmen folgen hat oder einen der schmerz vermeidet welcher keine daraus resultierende freude nach sich zieht auch gibt es niemanden der den schmerz an sich liebt sucht oder wuenscht nur weil er schmerz ist es sei denn es kommt zu zufaelligen umstaenden in denen muehen und schmerz ihm grosse freude bereiten koennen um ein triviales beispiel zu nehmen wer von uns unterzieht sich je anstrengender koerperlicher betaetigung ausser um vorteile daraus zu ziehen aber wer hat irgend ein recht einen menschen zu tadeln der die entscheidung trifft eine freude zu geniessen die keine unangenehmen folgen hat oder einen der schmerz vermeidet welcher keine daraus resultierende freude nach sich ziehtauch gibt es niemanden der den schmerz an sich liebt sucht oder wuenscht nur "
string = "präambel wir erleben neue politische zeiten mit vielfältigen herausforderungen für deutsch- land – sowohl international als auch national. deutschland ist weltweit ein anerkann- ter partner, aber nur mit einem neuen aufbruch für europa wird deutschland langfris- tig frieden, sicherheit und wohlstand garantieren können. die europäische union muss ihre werte und ihr wohlstandsversprechen bewahren und erneuern. nur eine starke europäische union ist der garant für eine zukunft in frieden, sicherheit und wohlstand. wir wollen eine neue dynamik für deutschland. nur so können wir das erreichte si- chern und ausbauen. unsere ausgangslage ist gut. die wirtschaft boomt, noch nie waren so viele menschen in arbeit und beschäftigung. das ist auch ergebnis der regierungszusammenarbeit von cdu, csu und spd. unsere heutige wirtschaftliche stärke eröffnet die chance, gerechtigkeit langfristig zu sichern. unser ziel ist ein nachhaltiges und inklusives wachstum, dessen erträge allen zugutekommen. wir wollen die kreativen potenziale in deutschland mobilisieren und die chancen der digitalisierung nutzen. deutschland braucht wirtschaftlichen und sozialen fortschritt, an dem alle teilhaben. wir wollen, dass der wohlstand bei allen menschen ankommt. das wahlergebnis hat gezeigt, dass viele menschen unzufrieden und verunsichert sind. daraus ziehen wir mit dem vorliegenden koalitionsvertrag und seiner politik die entsprechenden schlüsse. wir wollen sichern, was gut ist, aber gleichzeitig den mut zur politischen debatte, zu erneuerung und für veränderung beweisen. bürgerinnen und bürger haben ein starkes bedürfnis nach gemeinschaft, sicherheit im alltag, bewahrung der kulturellen identität, stabilität, einem guten miteinander und einer gestaltenden politik, die menschen auf augenhöhe zusammenbringt. millionen menschen engagieren sich in deutschland in sozialen, kulturellen und lokalen bewe- gungen sowie in gemeinde- und stadträten, kreistagen, kirchen und religionsge- meinschaften für unser gemeinwesen. gemeinsam mit ihnen wollen wir unser land besser, sicherer und gerechter machen.wir werden die probleme anpacken, welche die menschen in ihrem alltag bewegen, und setzen uns mutige ziele für die nächsten vier jahre. wir arbeiten für stabilität und zusammenhalt, für erneuerung und sicherheit und für die gleichwertigkeit der lebensverhältnisse in unserem land. die besonderen herausforderungen in ost- deutschland erkennen wir als gesamtdeutschen auftrag an. den sozialen zusammenhalt in unserem land wollen wir stärken und die entstande- nen spaltungen überwinden. wir nehmen die ängste der menschen ernst und wollen ihnen durch unsere gemeinsame arbeit umfassend begegnen. wir geben allen kin- dern und jugendlichen gleiche bildungschancen, damit leistung und talent über die persönliche zukunft entscheiden, nicht die soziale herkunft. wir schaffen neue per- spektiven für gute arbeit und mehr sicherheit im alter. wir wollen, dass die menschen bei uns die vielfältigen chancen nutzen und in si- cherheit leben können. familien stärken wir und sorgen dafür, dass familie und be- ruf besser vereinbar sind."
alphabet =  "abcdefghijklmnopqrstuvwxyz "
schlossel = "bacedgfthzujiklopmvsxyqwrn "
haufigkeit = dict()
haufigkeitalphabet = " enisratdhulcgmobwfkzpvjyxq"

def codeing(alphabet, schlossel, string):
    code = ""
    for g in string :
        if g in alphabet:
            M = alphabet.find(g)
            code = code + schlossel[M]
    return code

Statz = codeing(alphabet, schlossel, string)
print "Encode: " + (Statz)
Entschlosselt = codeing(schlossel, alphabet, Statz)
print "Decode: " + (Entschlosselt)


for i in Statz :
    haufigkeit[i] = haufigkeit.get(i, 0) + 1


liste = [(val,key) for key,val in haufigkeit.items()]
liste.sort()
liste.reverse()
print (liste)
bla = " "
for i in liste:
    if i[1] != ' ':
        bla = bla + i[1]

print(codeing(bla, haufigkeitalphabet, Statz))