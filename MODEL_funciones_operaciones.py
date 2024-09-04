import math
from VIEW_Plano_cartesiano import *

hay_x = 0


def suma(a,b):
    c=a+b
    return(c)


def resta(a,b):
    c=a-b
    return(c)


def mult(a,b):
    c=a*b
    return(c)


def div(a,b):

    if hay_x > 0 and b == 0:
        c = 10000000000000

    else:
        c=a/b
    return(c)


def sen(a):
    c = math.sin(a)
    return(c)


def cos(a):
    c = math.cos(a)
    return(c)


def tg(a):
    c = math.tan(a)
    return(c)


def asen(a):
    c = math.asin(a)
    return(c)


def acos(a):
    c = math.acos(a)
    return(c)


def atg(a):
    c = math.atan(a)
    return(c)


def pi():
    c = math.pi
    return(c)


def Euler():
    c = math.e
    return(c)


def e(a):
    c = Euler() ** a
    return(c)


def log(a,b):
    c = math.log(a,b)
    return(c)


def ln(a):
    c = math.log(a)
    return(c)


def expo(a,b):
    c = a ** b
    return(c)


def raiz(a,num):
    res = num ** ( 1 / a)
    return res


def valor_ads(a):

    if a >= 0:
        return a
    else:
        return -a
    

def not_cint(a,b):

    c = a * 10 ** b

    return c


def porcentaje(a,b):

    c = a * ( b / 100 )

    return c


def base_diez(a):

    c = 10 ** a

    return c

  
def factorial(a):

    if int(a) == 0 or int(a) == 1:
        c = 1
        return c
    
    else:
        
        c = 1
        i=0
        for i in range(1,int(a)+1):
            c *= i
        
        return c


def operaciones_simples (ecu):

    alfabetico=["m",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alfabetico_p=["M",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    jerarquia_cor = ["simples_cor","expo_cor", "raizc_cor", "multi_cor", "divic_cor","syre_cor"]
    jerarquia = ["simples","expon", "raizc", "multi", "divic","syre"]
    i=0
    j=0
    l=0
    L=0
    cor_in=0
    l_ecu=len(ecu)
    exec("globals()[alfabetico[0]] = []")
    exec("globals()[alfabetico_p[0]] = 0")

    for i in range (i,l_ecu):


        termino = ecu[i]
        globales=globals()


        if termino == "(":
                
            for cor_in in range(cor_in,i):

                globales[alfabetico[j]].append(ecu[cor_in])
                
            globales[alfabetico[j]].append("¿")
                    
            while alfabetico[j] in globals():
                j+=1

            exec("globals()[alfabetico[j]] = []")
            exec("globals()[alfabetico_p[j]] = i")
            L+=1
            cor_in=i+1

        elif termino == ")":
         
            if l +1 == L:

                for cor_in in range(cor_in,i):

                    globales[alfabetico[j-1]].append(ecu[cor_in])

            else:

                for cor_in in range(cor_in,i):

                    globales[alfabetico[j]].append(ecu[cor_in])

            cor_in=i+1  
            l+=1
            j-=1

        elif l == L and l_ecu-1 == i:
            
            for cor_in in range(cor_in,l_ecu):

                if j == 0:

                    globales[alfabetico[j]].append(ecu[cor_in])

                else:

                    globales[alfabetico[j-1]].append(ecu[cor_in])
    
    c=l 

    for l in range (l,-1,-1):
         
        ecua = globales[alfabetico[l]]
        ecuacion = len(ecua)
        ñ=0

        for ñ in range(ñ,ecuacion):
             
            operador = ecua[ñ]
            ope = type(operador)

            if ope == str:

                if  operador == "w":

                    a = ecua [ñ-1]
                    op = factorial(a)

                    if jerarquia_cor[0] in globals():

                        globales[jerarquia_cor[0]].append(ñ-1)

                    else:

                        exec("globals()[jerarquia_cor[0]] = []")
                        globales[jerarquia_cor[0]].append(ñ-1)

                    if jerarquia[0] in globals():

                        globales[jerarquia[0]].append(op)

                    else:

                        exec("globals()[jerarquia[0]] = []")
                        globales[jerarquia[0]].append(op)
                 
                elif  operador == "p"  :

                    a = ecua [ñ-1]
                    b = ecua [ñ+1]
                    op = expo(a,b)

                    if jerarquia_cor[1] in globals():

                        globales[jerarquia_cor[1]].append(ñ-1)

                    else:

                        exec("globals()[jerarquia_cor[1]] = []")
                        globales[jerarquia_cor[1]].append(ñ-1)

                    if jerarquia[1] in globals():

                        globales[jerarquia[1]].append(op)

                    else:

                        exec("globals()[jerarquia[1]] = []")
                        globales[jerarquia[1]].append(op)
                
                elif operador == "r":

                    a = ecua [ñ-1]
                    b = ecua [ñ+1]
                    op = raiz(a,b)

                    if jerarquia_cor[2] in globals():

                        globales[jerarquia_cor[2]].append(ñ-1)

                    else:

                        exec("globals()[jerarquia_cor[2]] = []")
                        globales[jerarquia_cor[2]].append(ñ-1)

                    if jerarquia[2] in globals():

                        globales[jerarquia[2]].append(op)

                    else:

                        exec("globals()[jerarquia[2]] = []")
                        globales[jerarquia[1]].append(op)

                elif operador == "*" :

                    a = ecua [ñ-1]
                    b = ecua [ñ+1]
                    op = mult(a,b)

                    if jerarquia_cor[3] in globals():

                        globales[jerarquia_cor[3]].append(ñ-1)

                    else:

                        exec("globals()[jerarquia_cor[3]] = []")
                        globales[jerarquia_cor[3]].append(ñ-1)

                    if jerarquia[3] in globals():

                        globales[jerarquia[3]].append(op)

                    else:

                        exec("globals()[jerarquia[3]] = []")
                        globales[jerarquia[3]].append(op)

                elif operador == "/":

                    a = ecua [ñ-1]
                    b = ecua [ñ+1]
                    op = div(a,b)

                    if jerarquia_cor[4] in globals():

                        globales[jerarquia_cor[4]].append(ñ-1)

                    else:

                        exec("globals()[jerarquia_cor[4]] = []")
                        globales[jerarquia_cor[4]].append(ñ-1)

                    if jerarquia[4] in globals():

                        globales[jerarquia[4]].append(op)

                    else:

                        exec("globals()[jerarquia[4]] = []")
                        globales[jerarquia[4]].append(op)

        ecua_f = len(ecua)

        if l == 0:

            cont = ecua_f - 1

        else:

            cont = ecua_f + 1
        

        if jerarquia[0] in globals():

            ex = globales[jerarquia[0]]
            ex_c = globales[jerarquia_cor[0]]
            exp_l = len(globales[jerarquia[0]])
            i=0

            for i in range (i,exp_l):

                ecua[ex_c[i]]=ex[i]

        elif jerarquia[1] in globals():

            ra = globales[jerarquia[1]]
            ra_c = globales[jerarquia_cor[1]]
            raiz_l = len(globales[jerarquia[1]])
            i=0

            for i in range (i,raiz_l):
                ecua[ra_c[i]]=ra[i]

        elif jerarquia[2] in globals():

            mu = globales[jerarquia[2]]
            mu_c = globales[jerarquia_cor[2]]
            mult_l = len(globales[jerarquia[2]])
            i=0
            m=0

            for i in range (i,mult_l):

                ecua[mu_c[i]]=mu[i]
                del ecua [mu_c[i]+1]
                del ecua [mu_c[i]+1]
                m+=1

                if m < mult_l:

                    mu_c[i+1]-=2 
                    


        elif jerarquia[3] in globals():

            di = globales[jerarquia[3]]
            di_c = globales[jerarquia_cor[3]]
            div_l = len(globales[jerarquia[3]])
            i=0
             
            for i in range (i,div_l):
                ecua[di_c[i]]=di[i]
                del ecua [di_c[i]+1]
                del ecua [di_c[i]+1] 

        elif jerarquia[4] in globals():

            di = globales[jerarquia[4]]
            di_c = globales[jerarquia_cor[4]]
            div_l = len(globales[jerarquia[4]])
            i=0
             
            for i in range (i,div_l):
                ecua[di_c[i]]=di[i]
                del ecua [di_c[i]+1]
                del ecua [di_c[i]+1]

        ecua_f = len(ecua)

        while ecua_f > 1:

            ope_f= ecua[1]
            ope_f_t=type(ope_f)

            if ope_f_t == str:

                if ope_f == "+":

                    a = ecua[0]
                    b = ecua[2]
                    su = suma(a,b)
                    ecua[0] = su
                    del ecua [1]
                    del ecua [1]

                elif ope_f == "-":

                    a = ecua[0]
                    b = ecua[2]
                    re = resta(a,b)
                    ecua[0] = re
                    del ecua [1]
                    del ecua [1]

                else:
                    break

            elif ope_f_t == float:

                if ecua[0] == "-":

                    re = -ecua[1]
                    ecua[0] = re
                    del ecua[1]
            
            ecua_f = len(ecua)

        t=0
        ubi = globales[alfabetico_p[l]]
        ecuacion_fin=float(ecua[0])
        ecu[ubi] = ecuacion_fin
        t+=1
        p=0

        for p in range (p,cont):
            del ecu [ubi+1]

        l-=1
        
        for t in range (t,0,-1):

            if l == -1:

                beri_l= 0

            else:

                beri = globales[alfabetico[l]]
                beri_l=len(beri)-1
            
            for beri_l in range(beri_l,0,-1):

                if beri[beri_l] == "¿":

                    if c > l:

                        beri_r= globales[alfabetico[c]]
                        beri[beri_l] =beri_r[0]
                        c-=1
                        l=0
        
        if jerarquia[0] in globals():

            del globales[jerarquia[0]]
            del globales[jerarquia_cor[0]]

        elif jerarquia[1] in globals():

            del globales[jerarquia[1]]
            del globales[jerarquia_cor[1]]

        elif jerarquia[2] in globals():

            del globales[jerarquia[2]]
            del globales[jerarquia_cor[2]]

        elif jerarquia[3] in globals():

            del globales[jerarquia[3]]
            del globales[jerarquia_cor[3]]

        elif jerarquia[4] in globals():

            del globales[jerarquia[4]]
            del globales[jerarquia_cor[4]]   

    re_ecu = ecu[0]
    return re_ecu  


def operaciones_complejas(ecu):

    l_ecu=len(ecu)
    i = 0
    co=[]
    dif =0

    while i < l_ecu:

        f=l_ecu-dif

        if ecu[i] == "L":

            if ecu[i+1] == "(":

                cor_i_sub = i+2
                cor_f_sub = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:

                        cor_f_sub = i+j
                        break

                    elif ecu[i+j] == ")":                      
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

            if ecu[cor_f_sub+1] == "(":

                cor_i = cor_f_sub +2
                cor_f = 0
                cont_p = 0
                j = cor_f_sub+2

                for j in range (j,l_ecu):

                    if ecu[i+j] == ")" and cont_p == 0:

                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":                      
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

            ecua_sub = []
            ecua = []
            ecua.extend(ecu[cor_i:cor_f])
            resultado = operaciones_simples(ecua)
            ecua_sub.extend(ecu[cor_i_sub:cor_f_sub])
            resultado_sub = operaciones_simples(ecua_sub)
            co.append(log(resultado,resultado_sub))
            dif+=cor_f-cor_i+2
            i = cor_f+1

        elif ecu[i] == "o" :

            if ecu[i-1] == ")" :

                cor_f_1 = i-1
                cor_i_1 = 0
                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j = i-2

                for j in range (j,-1,-1):

                    if ecu[j] == "(" and cont_p == 0:

                        cor_i_1 = j+1
                        break

                    elif ecu[j] == "(" :
                        cont_p += 1
                    
                    elif ecu[j] == ")" :
                        cont_p -= 1

                j = 2

                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:

                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":                      
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua_1 = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado = operaciones_simples(ecua)
                ecua_1.extend(ecu[cor_i_1:cor_f_1])
                resultado_1 = operaciones_simples(ecua_1)
                diferencia = cor_f_1-cor_i_1
                l = 0

                for l in range (l,diferencia+2):
                    del co[-1]

                co.append(porcentaje(resultado_1,resultado))
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i] == "j" :

            if ecu[i-1] == ")" :

                cor_f_1 = i-1
                cor_i_1 = 0
                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j = i-2

                for j in range (j,-1,-1):

                    if ecu[j] == "(" and cont_p == 0:

                        cor_i_1 = j+1
                        break

                    elif ecu[j] == "(" :
                        cont_p += 1
                    
                    elif ecu[j] == ")" :
                        cont_p -= 1

                j = 2

                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:

                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":                      
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua_1 = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado = operaciones_simples(ecua)
                ecua_1.extend(ecu[cor_i_1:cor_f_1])
                resultado_1 = operaciones_simples(ecua_1)
                diferencia = cor_f_1-cor_i_1
                l = 0

                for l in range (l,diferencia+2):
                    del co[-1]

                co.append(not_cint(resultado_1,resultado))
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i] == "F" :

            if ecu[i-1] == ")" :

                cor_f_1 = i-1
                cor_i_1 = 0
                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j = i-2

                for j in range (j,-1,-1):

                    if ecu[j] == "(" and cont_p == 0:

                        cor_i_1 = j+1
                        break

                    elif ecu[j] == "(" :
                        cont_p += 1
                    
                    elif ecu[j] == ")" :
                        cont_p -= 1

                j = 2

                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:

                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":                      
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua_1 = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado = operaciones_simples(ecua)
                ecua_1.extend(ecu[cor_i_1:cor_f_1])
                resultado_1 = operaciones_simples(ecua_1)
                diferencia = cor_f_1-cor_i_1
                l = 0

                for l in range (l,diferencia+2):
                    del co[-1]

                co.append(div(resultado_1,resultado))
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i] == "r" :

            if ecu[i-1] == ")" :

                cor_f_1 = i-1
                cor_i_1 = 0
                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j = i-2

                for j in range (j,-1,-1):

                    if ecu[j] == "(" and cont_p == 0:

                        cor_i_1 = j+1
                        break

                    elif ecu[j] == "(" :
                        cont_p += 1
                    
                    elif ecu[j] == ")" :
                        cont_p -= 1

                j = 2

                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:

                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":                      
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua_1 = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado = operaciones_simples(ecua)
                ecua_1.extend(ecu[cor_i_1:cor_f_1])
                resultado_1 = operaciones_simples(ecua_1)
                diferencia = cor_f_1-cor_i_1
                l = 0

                for l in range (l,diferencia+2):
                    del co[-1]

                co.append(raiz(resultado_1,resultado))
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i] == "p" :

            if ecu[i-1] == ")" :

                cor_f_1 = i-1
                cor_i_1 = 0
                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j = i-2

                for j in range (j,-1,-1):

                    if ecu[j] == "(" and cont_p == 0:

                        cor_i_1 = j+1
                        break

                    elif ecu[j] == "(" :
                        cont_p += 1
                    
                    elif ecu[j] == ")" :
                        cont_p -= 1

                j = 2

                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:

                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":                      
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua_1 = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado = operaciones_simples(ecua)
                ecua_1.extend(ecu[cor_i_1:cor_f_1])
                resultado_1 = operaciones_simples(ecua_1)
                diferencia = cor_f_1-cor_i_1
                l = 0

                for l in range (l,diferencia+2):
                    del co[-1]

                co.append(expo(resultado_1,resultado))
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i]== "S":

            if ecu[i+1] == "(":

                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:

                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":                      
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado=operaciones_simples(ecua)
                resultado = sen(resultado)
                co.append(resultado)
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i]== "C":

            if ecu[i+1] == "(":

                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:

                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado=operaciones_simples(ecua)
                resultado = cos(resultado)
                co.append(resultado)
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i]== "T":

            if ecu[i+1] == "(":

                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:

                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado=operaciones_simples(ecua)
                resultado = tg(resultado)
                co.append(round(resultado,13))
                dif+=cor_f-cor_i+2
                i = cor_f
                i = cor_f+1

        elif ecu[i]== "s":

            if ecu[i+1] == "(":

                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:
                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado=operaciones_simples(ecua)
                resultado = asen(resultado)
                co.append(resultado)
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i]== "u":

            if ecu[i+1] == "(":

                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:
                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado=operaciones_simples(ecua)
                resultado = acos(resultado)
                co.append(resultado)
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i]== "t":

            if ecu[i+1] == "(":

                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:
                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado=operaciones_simples(ecua)
                resultado = atg(resultado)
                co.append(resultado)
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i]== "l":

            if ecu[i+1] == "(":

                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:
                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado=operaciones_simples(ecua)
                resultado = ln(resultado)
                co.append(resultado)
                dif+=cor_f-cor_i+2
                i = cor_f+1
                

        elif ecu[i]== "|":

            if ecu[i] == "|":

                cor_i = i+1
                cor_f = 0
                cont_p = 0
                j=1
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == "|" and cont_p == 0:
                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])

                if ecua[0] == "-":
                    del ecua[0]
                    ecua[0] = -ecua[0]

                resultado = valor_ads(ecua[0])
                co.append(resultado)
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i]== "w":

            if ecu[i+1] == "(":

                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:
                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado=operaciones_simples(ecua)
                resultado = factorial(resultado)
                co.append(resultado)
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i]== "B":

            if ecu[i+1] == "(":

                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:
                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado=operaciones_simples(ecua)
                resultado = base_diez(resultado)
                co.append(resultado)
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i]== "e":

            if ecu[i+1] == "(":

                cor_i = i+2
                cor_f = 0
                cont_p = 0
                j=2
                
                for j in range (j,l_ecu):
                    
                    if ecu[i+j] == ")" and cont_p == 0:
                        cor_f = i+j
                        break

                    elif ecu[i+j] == ")":
                        cont_p -= 1

                    elif ecu[i+j] == "(":
                        cont_p += 1

                ecua = []
                ecua.extend(ecu[cor_i:cor_f])
                resultado=operaciones_simples(ecua)
                resultado = e(resultado)
                co.append(resultado)
                dif+=cor_f-cor_i+2
                i = cor_f+1

        elif ecu[i] == "P":

            co.append(pi())
            i += 1

        elif ecu[i] == "E":

            co.append(Euler())
            i += 1
                
        else:
            co.append(ecu[i])
            i += 1     
            
    resultado_fin=operaciones_simples(co)
    return resultado_fin


def operaciones_x(fig,ax,entrada,ecu,frame,frame_funciones,color_select):

    x = []
    y = []
    i = 0
    lista = []
    hay_log=ecu.count("L")
    hay_ln=ecu.count("l")
    hay_asen = ecu.count("s")
    hay_acos = ecu.count("u")
    hay_raiz = ecu.count("r")
    hay_W = ecu.count("w")
    hay_tn = ecu.count("T")

    if hay_log > 0 or hay_ln > 0 or hay_raiz:
        l=0.2
        x.append(l)

        while l < 50:
            x.append(round(l+0.2, 5))
            l += 0.2

    elif hay_asen > 0 or hay_acos > 0:
        l=-1
        x.append(l)

        while l < 1:
            x.append(round(l+0.2, 5))
            l += 0.2

    elif hay_W > 0:
        l=0
        x.append(l)

        while l < 20:
            x.append(round(l+0.2, 5))
            l += 0.2

    elif hay_tn > 0:
        l = -50
        x.append(l)

        while l < 50:
            x.append(l+0.025)
            l += 0.025

        

    else:
        l=-50
        x.append(l)

        while l < 50:
            x.append(round(l+0.2, 5))
            l += 0.2

    for i in range (i,len(x)):

        ecuacion = []
        j = 0

        for j in range (j,len(ecu)):

            siesx=ecu[j]

            if siesx == "x":
                ecuacion.append(x[i])

            else:
                ecuacion.append(ecu[j])

        resultado_y = operaciones_complejas(ecuacion)
        y.append(resultado_y)

    plot_graph(fig,ax,frame,x,y,entrada,frame_funciones,color_select,hay_tn)
    

def operacion_principal(fig,ax,entrada,entrada_result,ecua,frame,frame_funciones,color_select):

    n=len(ecua)
    P_dig=""
    ecu = []
    i = 0

    global hay_x

    try:
        for i in range(i,n):

            elem=ecua[i]
            em=type(elem)
            terminos_1=ecua[i]
            lem=ord(terminos_1)
            if em == str:

                if lem >= 48 and lem <=57:
                    P_dig= P_dig + elem

                elif lem == 43:                    
                    if P_dig != "":
                        ecu.append(float(P_dig))
                        P_dig=""
                    ecu.append("+")              

                elif lem == 45:
                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("-")

                elif lem == 215:
                            
                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("*")

                elif lem == 47:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("/")

                elif lem == 61:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("=")

                elif lem == 46:

                    if lem >= 48 and lem <= 57:

                        P_dig= P_dig + elem

                    else:
                        P_dig= P_dig + elem

                elif lem == 83:
                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("S")

                elif lem == 67:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("C")

                elif lem == 84:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("T")

                elif lem == 115:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("s")

                elif lem == 117:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("u")

                elif lem == 116:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("t")

                elif lem == 80:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("P")

                elif lem == 69:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("E")

                elif lem == 101:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("e")

                elif lem == 120:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("x")

                elif lem == 121:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("y") 

                elif lem == 76:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("L")

                elif lem == 108:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("l")

                elif lem == 112:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("p")

                elif lem == 114:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("r")

                elif lem == 40:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("(")

                elif lem == 41:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append(")")

                elif lem == 118:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("v")

                elif lem == 70:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("F")

                elif lem == 106:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("j")

                elif lem == 111:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("o")

                elif lem == 66:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("B")

                elif lem == 119:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("w")

                elif lem == 124:

                            if P_dig != "":
                                ecu.append(float(P_dig))
                                P_dig=""
                            ecu.append("|")

                else:
                    raise ValueError(entrada_result.delete(0,"end"),entrada_result.insert(0,"Syntax Error"))

    
        if P_dig != "":
            ecu.append(float(P_dig))

        hay_x = 0

        i = 0

        for i in range (i,len(ecu)):

            if ecu[i] == "x":
                hay_x = 1

        if hay_x > 0:

            hay_op = 0
            for i in ecu:
                if i == ("+","-","*","/","=","S","C","T","s","u","t","P","E","e","L","l","p","r","v","F","j","o","B","w","|"):
                    hay_op += 1
                    break
            
            if hay_op == 1:
                 
                respuesta = operaciones_x(fig,ax,entrada,ecu,frame,frame_funciones,color_select)
                return True
            
            else:
                
                entrada_result.delete(0,"end")
                entrada_result.insert(0,"Syntax Error")

        else:

            respuesta = operaciones_complejas(ecu)
            entrada_result.delete(0,"end")
            entrada_result.insert(0,respuesta)
            return False

    except Exception as e:
         
        entrada_result.delete(0,"end")
        entrada_result.insert(0,"Syntax Error")