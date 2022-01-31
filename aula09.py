frase=('Eu gosto de me lambejar todo')
#para cortar/manipular strings
print(frase[1:29:2])

frase2=("""¥Î èh Ç   éÎþÿÿD  ATUWVSHƒì H‹=Î …ÒH‰Í‰ÓM‰Ä‰uB‹; …ÀtZèb¥ M‰à1ÒH‰éè•· ‰Æƒû„ª   …Û„¢   ‰ðÇÿÿÿÿHƒÄ [^_]A\Ãè*¥ Cÿƒøw0M‰à‰ÚH‰éè5ýÿÿ…À…   1öëÇf„     ƒû…¹   è¢¨ M‰à‰ÚH‰éè%· …À‰ÆuŒƒûu‡1ÒM‰àH‰éè
· 1ÒM‰àH‰éè· 1ÒM‰àH‰éèÓüÿÿƒû…`ÿÿÿf.„     M‰à‰ÚH‰éèã¶ M‰à‰ÚH‰é‰Æè¤üÿÿ…À¸    Dðé3ÿÿÿD  M‰à‰ÚH‰éè³¶ …À‰Æ…Yÿÿÿƒû…CÿÿÿM‰à1ÒH‰éècüÿÿéüþÿÿM‰àº   H‰éèn¶ ‰ÆéÔþÿÿ€    HƒìHH‹UÍ ƒúÇ     t
HƒÄHéqþÿÿL‰D$8‰T$4H‰L$(è½§ èH« L‹D$8‹T$4H‹L$(HƒÄHéAþÿÿD‹McÂAƒÂF¶B¶DF¶\B¶LD‰AÁáD	ÈAÁãÁáD	Ø	ÈÃ„     ATUWVSHƒì0¸   ‰Öâ   H‰ËÁê)Ð÷Æ   ‰dN  „D  ‰÷A‰ñÇXN""")

#encontrar letra em caracter x
print(frase2[59])

#para contar determinado caracter
print(frase2.count('ÿ'))

#para contar caracteres:
print(len(frase2))

#para trocar palavras:
print(frase.replace('gosto','não gostei'))

#para procurar palavra
print('lambejar todo' in frase)

#para encontrar palavra
print(frase2.find(''))

#separar string (palavras em strings) - lista
dividido=(frase.split())
#encontrar a palavra na lista, e o seu caracter
print(dividido[4][5])


