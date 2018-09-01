
# coding: utf-8

# In[7]:


pylab inline


# In[8]:



#VARIABLES GENERALES
#Deficinion de variables a tener en cuenta en la trata de personas 
#Edad ENTRE 12 Y 35 AÃ‘OS-E
#Genero-F-M
#Nivel educativo-BARRICLLER-B, PRIMARIA-P, UNIVERSITARIO O PROFESIONAL-U 
#Uso de redes sociales- FACEBOOK-F, INSTAGRAM-I
E=0.4
#rango binario edad dado ---victima----
Eda=0.43

#prior
Facebook=0.57
#dado victima
Fa = 0.8
#prior
Instagram=0.28
#dado victima
Insta = 0.8



#POBLACION TOTAL COLOMBIANA 
BAJAESC= 0.4 

#ESCOLARIDAD EN REGIONES DE TRATA maximo bachillerato
ANT=0.07
BOG=0.1
CAL=0.07
CUND=0.07
NAR=0.06
RIS=0.07
SAN=0.07
VALL=0.08


#porcentaje poblacion colombia prior regiones
ANTI = 0.135
BOGO = 0.17
CALD = 0.021
CUNDIN = 0.05
NARI = 0.03
RISA = 0.02
SANTA = 0.04
VALLEDE = 0.1



#VARIABLES ENFOCADAS A LA TRATA 
#lugar de residencia de riesgo-L
#casos de trata regionales- ESTIMADOS REALES 

ANTIOQUIA=0.000039      #220.0 personas real- reportados 11 por cada caso reportado 20 ocultos 
BOGOTA=0.0000026  
CALDAS=0.000062
CUNDINAMARCA= 0.000018
NARINO=0.00026
RISARALDA=0.00023
SANTANDER=0.00051
VALLEDELCAUCA=0.00058

#prob prior peligro trata colombia
p= (ANTIOQUIA+BOGOTA+CALDAS+CUNDINAMARCA+NARI+RISARALDA+SANTANDER+VALLEDELCAUCA)/8


#Female - male prior
F=0.5
M=0.5

#relacion de casos registrados de trata mujeres y hombres

MUJERES=0.84
HOMBRES=0.16


#variable True si la persona esta entre los 12 y 35 años 
EDAD = False
#usa mucho facebook?
Uso_face = False
#usa mucho instagram?
Uso_insta = False
#Region. Posibles: Antioquia, Bogota, Caldas, Cundinamarca, Narino, Risaralda, Santander, Valledelcauca
Region = 0
#tiene mas estudios que el bachillerato?
Scholar = False
#genero
MALE = False


#arreglo de priors ordenados
priors = [E, Facebook, Instagram, [ANTI, BOGO, CALD, CUNDIN, NARI, RISA, SANTA, VALLEDE], [BAJAESC*ANTI, BAJAESC*BOGO, BAJAESC*CALD, BAJAESC*CUNDIN, BAJAESC*NARI, BAJAESC*RISA, BAJAESC*SANTA, BAJAESC*VALLEDE],M]



#criterios
num_crit = 6
#vector de desiciones 0 es no se preguntó, 1 si se tuvo respuesta
desitions = zeros(num_crit)


# In[3]:


#funcion que retorna el vector de la probabilidad condicional de ser victima dependiendo de los criterios que se escojan. 
#El vector "vec" es binario y representa las variables a tener en cuenta ("0" si no, "1" si si).
def vector_probs( vec, EDAD, Uso_face, Uso_insta, Region, Scholar, MALE):
    stuff = zeros(num_crit)
        
    if vec[0]!= 0:
        if EDAD == True:
            stuff[0] =  Eda/E
        else:
            stuff[0] = (1 - Eda)/(1-E)
    
    if vec[1]!= 0:
        if Uso_face == True:
            stuff[1] = Fa/Facebook
        else:
            stuff[1] = (1-Fa)/(1-Facebook)
    if vec[2]!= 0:
        if Uso_insta == True:
            stuff[2] = Insta/Instagram
        else:
            stuff[2] = (1-Insta)/(1-Instagram)
    
    if vec[3]!= 0:
        if Region == 1:
            stuff[3] = ANTI*ANTIOQUIA/p
        if Region == 2:
            stuff[3] = BOGOTA*BOGO/p
        if Region == 3:
            stuff[3] = CALDAS*CALD/p
        if Region == 4:
            stuff[3] = CUNDINAMARCA*CUNDIN/p
        if Region == 5:
            stuff[3] = NARINO*NARI/p
        if Region == 6:
            stuff[3] = RISARALDA*RISA/p
        if Region == 7:
            stuff[3] = SANTANDER*SANTA/p
        if Region == 8:
            stuff[3] = VALLEDELCAUCA*VALLEDE/p
        
    
    
    if vec[4]!= 0:
        if Scholar == True:
            if Region == 1:
                stuff[4] = ANT/(BAJAESC*ANTI)
            if Region == 2:
                stuff[4] = BOG/(BAJAESC*BOGOTA)
            if Region == 3:
                stuff[4] = CAL/(BAJAESC*CALDAS)
            if Region == 4:
                stuff[4] = CUND/(BAJAESC*CUNDINAMARCA)
            if Region == 5:
                stuff[4] = NAR/(BAJAESC*NARINO)
            if Region == 6:
                stuff[4] = RIS/(BAJAESC*RISARALDA)
            if Region == 7:
                stuff[4] = SAN/(BAJAESC*SANTANDER)
            if Region == 8:
                stuff[4] = VALL/(BAJAESC*VALLEDELCAUCA)
        else:
            if Region == 1:
                stuff[4] = (1-ANT)/(1-BAJAESC*ANTI)
            if Region == 2:
                stuff[4] = (1-BOG)/(1-BAJAESC*BOGOTA)
            if Region == 3:
                stuff[4] = (1-CAL)/(1-BAJAESC*CALDAS)
            if Region == 4:
                stuff[4] = (1-CUND)/(1-BAJAESC*CUNDINAMARCA)
            if Region == 5:
                stuff[4] = (1-NAR)/(1-BAJAESC*NARINO)
            if Region == 6:
                stuff[4] = (1-RIS)/(1-BAJAESC*RISARALDA)
            if Region == 7:
                stuff[4] = (1-SAN)/(1-BAJAESC*SANTANDER)
            if Region == 8:
                stuff[4] = (1-VALL)/(1-BAJAESC*VALLEDELCAUCA)
               
                
    if vec[5]!= 0:
        if MALE == False:
            stuff[5] = HOMBRES/M
        else:
            stuff[5] = (1-HOMBRES)/(1-M)
    
    return stuff
    


# In[4]:


#esta funcion retorna el riesgo tomando solo la informacion de interes especificada en el vector de valores binarios.
def partial_info_risk(stuff, vec):
    conditional_proba = 1.0
    for k in range(len(stuff)):
        if vec[k]!=0:
            if stuff[k]!=0:
                conditional_proba = conditional_proba*stuff[k]
    
    return conditional_proba*p
    
    
    
#esta funcion calcula la entropia (EN BITS) de las distribuciones para la probabilidad de ser victima con las condiciones a tomar por entrada
def entropy( vec):
    value = 0.0
    if all(k==0 for k in vec) == True:
        value = -1*( p*log2(p) + (1-p)*log2(1-p) )
        
    else:
        
        iterator = [True, False]
        arreglo=[]
        for i in iterator:
            for j in iterator:
                for k in iterator:
                    for m in range(8):
                        for n in iterator:
                            for h in iterator:
                                
                                probabs = vector_probs( vec, i, j, k, m+1, n, h)
                                
                                condi = partial_info_risk(probabs, vec)
                                
                                pris = 1.0
                                for g in range(num_crit):
                                    if vec[g] !=0:
                                        
                                        if g == 0:
                                            if i == True:
                                                pris=pris*priors[g]
                                            elif i == False:
                                                pris=pris*(1-priors[g])
                                        
                                        elif g == 1:
                                            if j == True:
                                                pris=pris*priors[g]
                                            elif j == False:
                                                pris=pris*(1-priors[g])
                                            
                                        elif g == 2:
                                            if k == True:
                                                pris=pris*priors[g]
                                            elif k == False:
                                                pris=pris*(1-priors[g])
                                        
                                        elif g == 3:
                                            pris = pris*priors[g][m]
                                            
                                        elif g== 4:
                                            if n == True:
                                                pris = pris*priors[g][m]
                                            elif n == False:
                                                pris = pris*(1-priors[g][m])
                                                
                                        elif g == 5:
                                            if h == True:
                                                pris=pris*priors[g]
                                            elif h == False:
                                                pris=pris*(1-priors[g])
                                            
                                temp = -1*( pris*condi*log2(condi) + pris*(1-condi)*log2(1-condi) )
                                        
                                #if any(l == temp for l in arreglo)==False:
                                contador = 0
                                longi=len(arreglo)
                                for hola in range(longi):    
                                    if arreglo[hola] == temp:
                                        contador +=1
                                if contador == 0:
                                    arreglo.append(temp)
                                
        for h in arreglo:
            value += nan_to_num(h)
        
    return value
                                

#información mutua de las variables de interes en vec1, junto con las variables de interés en vec2
def mutual_info(vec1, vec2):
    return entropy(vec1) - entropy(vec2)

 


# In[5]:


#Ahora hacemos la matriz de correlación

info_matrix = zeros((6,6))
for i in range(6):
    for j in range(6):
        vec1 = zeros(6)
        vec1[i] = 1
        vec2 = zeros(6)
        vec2[j] = 1
        info_matrix[i,j] = mutual_info(vec1, vec2)
        
info_matrix


# In[6]:



fig = plt.figure(figsize=(9,7))
plt.imshow(matrix(info_matrix), origin='lower', aspect='auto', cmap='hot' )
plt.xlabel('Preguntas' , fontsize = 20)
plt.ylabel('Preguntas', fontsize = 20)
plt.title('Información mutua', fontsize = 20)
plt.colorbar(label = 'Bits',fontsize = 20)
plt.savefig('Info correlations.png')





# In[ ]:


#ahora hacemos el análisis de entropía por pregunta

entropy_Questions = zeros(6)
for i in range(6):
    vec = zeros(6)
    vec[i] = 1
    entropy_Questions[i] = entropy(vec)
    
entropy_Questions




# In[ ]:


fig = plt.figure(figsize=(15,10))
plt.rcParams.update({'font.size': 22})
plt.plot(linspace(1,6,6),entropy_Questions,linewidth=2)
plt.xlabel('Preguntas' , fontsize = 20)
plt.ylabel('Entropía(Bits)', fontsize = 20)
plt.title('Entropía preguntas', fontsize = 30)
plt.legend()
plt.savefig('Questions entropy.png')

