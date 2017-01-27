
# coding: utf-8

# 
# ### Course: Applied Economic Analysis I 

#  # Python Assignment 
# <p style="text-align: justify;">*Theoretical background and numerical simulation of an agglomeration model based on Michael Pflueger (2001): A simple analytically solvable, Chamberlinian agglomeration model.*</p>
# 

# Names| ANR's
# :------------: | :-------------:
# Aravanis Spyridon | 356138
# Ellinas Georgios | 370257
# Mantas Georgios | 245448
# 
# 
# 
# 
# 
# 

# ### Table of Contents 
# 
# <b id="i1">[Question](#b1)</b>
# 
# <b id="i2">[Motivation](#b2)</b>
# 
# <b id="i3">[Method](#b3)</b>
# 
# <b id="i4">[Answer](#b4)</b> 
# 
# <b id="i5">[Main Assumptions](#b5)</b> 
# 
# <b id="i6">[Theoretical Backround of Model](#b6)</b> 
# 
# * <b id="i7">[Consumers](#b7)</b> 
# 
# * <b id="i8">[Agriculture](#b8)</b> 
# 
# * <b id="i9">[Manufacturing](#b9)</b> 
# 
# * <b id="i10">[Price Index](#b10)</b> 
# 
# * <b id="i11">[Equilibrium demand and profits](#b11)</b> 
# 
# * <b id="i12">[Utility for entrepreneurs](#b12)</b> 
# 
# <b id="i13">[Simulation](#b13)</b>
# 
# (i) <b id="i4">[Higher transport costs multiplier $\pmb{(\tau)}$](#b14)</b>
# 
# (ii) <b id="i5">[Stronger taste for variety (lower $\pmb{\sigma}$)](#b15)</b>
# 
# (iii) <b id="i6">[Smaller share of immobile people](#b16)</b>
# 
# <b id="i17">[Conclusion](#b17)</b> 
# 
# <b id="i18">[Appendix](#b18)</b> 

# ## <b id="b1">Question</b>
# 
# <p style="text-align: justify;">Which are the main reasons why some cities aggregate a significant part of production activity attracting more and more firms in contrast to other cities that remain small and degraded in productivity terms? Could we really explain the simultaneous existence of small and large cities?</p>
# 

# ## <b id="b2">Motivation</b>
# 
# <p style="text-align: justify;">Our main motivation is to understand the complementarity between firms and workers. On the one hand, firms have the incentive to be established in cities in which there are productive,efficient and skilled workers and on the other hand, skilled workers are inclined to be concentrated in cities in which numerous companies are located. We try to decipher which are the the agglomeration and dispersion forces that are behind of this tendency. Forces that mainly impel companies to be established in already economically and productively developped cities. How factors like transaction costs, skilled or unskilled labor force affect the shifting of firms from one region to another?</p>

# ## <b id="b3">Method</b>
# 
# <p style="text-align: justify;">Through simulation process and using the parameter values $\rho=\rho^*=1$ (share of unskilled labor in the home and foreign region respectively), $\sigma=6$ (elasticity of substitution between manufacturing goods) and $\alpha=0.3$ (size of the manufacturing sector) as Pflueger uses in his paper, we illustrate graphs and explain how several factors lead to agglomeration (or dispersion) forces. In particular, we consider the effects of:  
# (i) higher transport costs (τ),  
# (ii) stronger taste for variety (lower σ),  
# (iii) smaller share of people that are immobile (unskilled labor).  
# Also we try to depict the effect of agglomeration on the real wage of workers (immobile consumers) in the two regions concerning the first two examined cases.</p>

# ## <b id="b4">Answer</b>
# 
# <p style="text-align: justify;">It can be concluded that higher transport costs weaken the agglomeration forces and decreases the wage of unskilled workers in segregated cities. Furthermore, lower elasticity of substitution between manufacturing goods weakens dispersion forces and increases the wage of unskilled labor force in cities that concentrate a significant part of production activity. Finally, we observe that smaller share of immobile workers enhances agglomeration forces making some cities more attractive for some companies.</p>

# ## <b id="b5">Main assumptions</b>
# 
# <p style="text-align: justify;">The main assumptions of the Pflueger's model are the following ones (we use different notations than the corresponding ones of the paper which are presented in the appendix):</p>
# 
# * <p style="text-align: justify;">The world is composed by two countries (home and foreign country, which the latter is denoted by an asterisk). We will consider that countries play the same role as cities and through this way we can answer the question imposed.</p>
# 
# * Two factors/inputs of production: skilled $(N)$ and unskilled labour $(L)$.
# * Two production sectors: agricultural and manufacturing.
# * Agricultural good is homogenous, traded without transport costs and produced perfectly competitively using unskilled labour as the only input.
# * <p style="text-align: justify;">Manufacturing goods are differentiated and produced by monopolistically competitive firms which use skilled and unskilled labour as inputs. Also, manufacturing goods are traded with transport costs.</p>
# * <p style="text-align: justify;">Unskilled labour is intersectorally mobile (moves only between the sectors of one country), while skilled labour-entrepreneurs-is internationally mobile (moves between countries). Entrepreneurs run one manufacturing firm each of them and choose to move to the country in which they have the higher utility.</p>
# * Both countries have identical preferences, technology and trade costs.  

# ## <b id="b6">Theoretical background of the model</b>  
#  
# ### <b id="b7">Consumers</b>  
# The quasi-linear utility function of consumers is given by:
# <b id="f1">$$U=C_{A}+\xi \ln C_{X} \tag{1}$$ </b> 
#  
# Subject to consumption of manufacturing goods:
# <b id="f2">$$C_{X}=\left[\sum_{i=1}^{N+N^\ast}\ x_{i}^{\displaystyle\frac{(\sigma-1)}{\sigma}}\right]^{\displaystyle\frac{\sigma}{(\sigma-1)}} \tag{2}$$</b> 
# 
# and income/wage level:
# <b id="f3">$$w=p_{A}C_{A}+\sum_{i=1}^{N+N^\ast}\ p_{i}x_{i} \tag{3}$$</b>
# 
# <p style="text-align: justify;">where $C_{A}$ represents the consumption for agricultural goods, $\xi$ is the size of market for manufacturing goods, $C_{X}$ is the total consumption for manufacturing goods, $x_{i}$ and $p_{i}$ are the quantity and price of manufacturing good i respectively,$\sigma$ is the elasticity of substitution bewteen manufacturing goods and $N+N^*$ is the total number of skilled workers and consequently the total number of manufacturing firms.</p>
# 
# <p style="text-align: justify;">Utility maximization, using the equations <b id="a1">[(1)](#f1)</b>,  <b id="a2">[(2)](#f2)</b> and <b id="a3">[(3)](#f3)</b> gives the demand functions for every manufacturing good $x_{i}$, for all the manufacturing goods and for agricultural good as follows:</p>
# 
#  
# <b id="f4">$$C_{x}=\left(\frac{1}{P}\right) p_{A}\xi \tag{4}$$</b>
# 
# <b id="f5">$$x_{i}=p_{A}\xi p_i^{-\sigma}P^{\sigma-1} \tag{5}$$</b>
# 
# <b id="f6">$$C_{A}=\frac{w}{p_{A}}-\xi \tag{6}$$</b>
# 
# where the following constitutes the price index for manufacturing goods:
#  
# <b id="f7">$$P= \left[\sum_{i=1}^{N+N^\ast}\ p_i^{1-\sigma} \right]^{\displaystyle \frac{1}{1-\sigma}} \tag{7}$$</b>
# 
# 
# ### <b id="b8">Agriculture</b>  
# 
# <p style="text-align: justify;">Perfect competition in agricultural sector ensures that this good is sold at price equal to its marginal product, which is equal to 1, because the production function is $X_{A}=L_{A}$ in both countries.</p>
#  
# <b id="f8">$$p_{A}=w_{L}=p_{A}^{\ast}=w_{L}^{\ast}=1 \tag{8}$$</b>
# 
# <p style="text-align: justify;">Simplified condition <b id="a8">[(8)](#f8)</b> ensures that the unskilled labor which works in countryside/hinterland do not have any incentive to move because the wages are the same between the two countries. That is why L is immobile.</p>  
# 
# ### <b id="b9">Manufacturing</b>  
# 
# <p style="text-align: justify;">Entrepreneurs in home city sell their differentiated products above cost and in the same price because there is monopolistic competition. The price that every entrepreneur sets is given by maximizing her profits:</p>
# 
# $$\pi_{i}=p_{i}x_{i}-c_{x}w_{L}x_{i} \tag{8'}$$
# 
# with respect to equation <b id="a5">[(5)](#f5)</b>. Therefore, the corresponding price in the home country is:
# 
# <b id="f9">$$p_{i}^{home}=\left(\frac{\sigma}{\sigma-1}\right)c_{x}w_{L} \tag{9}$$</b> 
# 
# And similarly the price for the exported manufacturing goods is:
#  
# <b id="f10">$$p_{i}^{export}=\left(\frac{\sigma}{\sigma-1}\right)\tau c_{x}w_{L} \tag{10}$$</b>
# 
# <p style="text-align: justify;">Ιt is apparent that the price which the manufacturing firm charges for foreign country (exports) is higher than the price which it charges for home country due to transport costs.</p>
# 
# Αlso, the entrepreneur’ profits in home country are equal to:
# 
# <b id="f11">$$w_{H}=(p_{i}^{home}-c_{x}w_{L})x_{i}^{home}pop+(p_{i}^{export}-\tau c_{x}w_{L})x_{i}^{export}pop^{\ast} \tag{11}$$</b>
# 
# Using equations <b id="a9">[(9)](#f9)</b>, <b id="a10">[(10)](#f10)</b> and <b id="a11">[(11)](#f11)</b> we have:
# 
# <b id="f12">$$w_{H}=\left(\frac{c_{x}w_{L}}{(\sigma-1)}\right)(x_{i}^{home}pop+\tau x_{i}^{export}pop^{\ast}) \tag{12}$$</b>
# 
# From equation <b id="a12">[(12)](#f12)</b> we can construct the corresponding entrepreneur’s wage in the foreign country $w^{\ast}$:
# 
# $$w_{H}^{\ast}=\left(\frac{c_{x}w_{L}}{(\sigma-1)}\right)(x_{i}^{home}pop^{\ast}+\tau x_{i}^{export}pop) \tag{12'}$$
# 
# ### <b id="b10">Price Index</b>  
# 
# <p style="text-align: justify;">However, entrepreneurs do not care only about their profits but also the price index/ consumption basket in the country that they locate, therefore they care for their real profits. From equation <b id="a7">[(7)](#f7)</b> the price index for manufacturing goods is alternatively written:</p>
#  
# <b id="f13">$$P=\left[N(p_i^{home})^{1-\sigma}+N^{\ast}(p_i^{export})^{1-\sigma}\right]^{\displaystyle\frac{1}{(1-\sigma)}} \tag{13}$$</b>
# 
# From <b id="a9">[(9)](#f9)</b>, <b id="a10">[(10)](#f10)</b> and <b id="a13">[(13)](#f13)</b> we have:
# 
# <b id="f14">$$P=\left(\frac{\sigma c_{x} w_{L}}{\sigma-1} \right)\left[N+N^{\ast} \tau^{1-\sigma}\right]^{\displaystyle\frac{1}{1-\sigma}}=\left(\frac{\sigma c_{x} w_{L}}{\sigma-1} \right) n^{\displaystyle\frac{1}{(1-\sigma)}} \tag{14}$$</b>
# 
# 
# <b id="f15">$$P^{\ast}=\left(\frac{\sigma c_{x} w_{L}}{\sigma-1} \right)\left[N^{\ast}+N \tau^{1-\sigma}\right]^{\displaystyle\frac{1}{1-\sigma}}=\left(\frac{\sigma c_{x} w_{L}}{\sigma-1} \right) {n^{\ast}}^{\displaystyle\frac{1}{(1-\sigma)}} \tag{15}$$</b>
# 
# Equations <b id="a14">[(14)](#f14)</b> and <b id="a15">[(15)](#f15)</b> give the price index in the home and foreign country respectively.
# 
# Using equations <b id="a14">[(14)](#f14)</b> and <b id="a15">[(15)](#f15)</b>:
# 
# <b id="f16">$$\frac{P}{P^{\ast}}=\left[\frac{N+N^{\ast} \tau^{1- \sigma}}{N^{\ast}+N \tau^{1-\sigma}}\right]^{\displaystyle\frac{1}{(1- \sigma)}}=\left(\frac{n}{n^{\ast}}\right)^{\displaystyle\frac{1}{(1- \sigma)}} \tag{16}$$</b>
# 
# <p style="text-align: justify;">This equation <b id="a16">[(16)](#f16)</b> explains how expensive or cheap the home country is relative to the foreign country. Taking the partial derivatives with respect to (i) transportation costs $(\tau)$ and (ii) the number of effective firms in the home country $(n)$ we observe the following results:</p>
# 
# * <p style="text-align: justify;">The higher the number of entrepreneurs in the home country and consequently the number of effective firms, the lower the price index in the home country relative to foreign country’s index. The higher variety in home country is beneficial for its entrepreneurs who want to locate on it $\to$ agglomeration effect</p>
# 
# * <p style="text-align: justify;">The higher the transport costs, the higher the price index in the home country relative to foreign price index while it becomes more expensive to import goods from the foreign country.When $\tau>1$ entrepreneurs in home country put a lower weight in variety of foreign county’s goods.In the extreme case $\tau=1$ (freeness of trade) the price index in both countries is the same and entrepreneurs do not care where they locate while they can export to the other country without any cost.</p>
# 
# <p style="text-align: justify;">Until now, our analysis takes into account only the cost of living/price index as we assume that the wages $w_{H}$ remain the same and only the cost of living changes.However, when a lot of entrepreneurs locate in home country then also $w_{H}$ decreases because every entrepreneur has to compete with more entrepreneurs who locate in the home country and share the same market with them. In this case, the home country becomes less attractive $\to$ dispersion effect. For this reason, we have to find the real profits. </p>
# 
# ### <b id="b11">Equilibrium demand and profits</b>  
# 
# <p style="text-align: justify;">First of all, the quantities that one firm in the home country sells domestically and abroad are the following (using equations <b id="a5">[(5)](#f5)</b>, <b id="a9">[(9)](#f9)</b>, <b id="a14">[(14)](#f14)</b> and <b id="a5">[(5)](#f5)</b>, <b id="a10">[(10)](#f10)</b> and <b id="a15">[(15)](#f15)</b>):</p>
# 
# 
# <b id="f17">$$x_{i}^{home}=\left(\frac{\xi p_{A}(\sigma-1)}{\sigma c_{x} w_{L}}\right) \left(\frac{1}{N+N^{\ast} \tau^{1- \sigma}}\right)=\left(\frac{\xi p_{A}}{ p_{i}^{home}}\right)\left(\frac{1}{n}\right) \tag{17}$$</b>
# 
# 
# <b id="f18">$$x_{i}^{export}=\left(\frac{\xi p_{A}(\sigma-1)}{\sigma c_{x} w_{L}}\right) \left(\frac{\tau^{-\sigma}}{N^{\ast}+N \tau^{1- \sigma}}\right)=\left(\frac{\xi p_{A}}{ p_{i}^{home}}\right)\left(\frac{\phi}{\tau n^\ast}\right) \tag{18}$$</b>
# 
# Therefore, the real profits of entrepreneur in home country are given by equations <b id="a12">[(12)](#f12)</b>, <b id="a17">[(17)](#f17)</b> and <b id="a18">[(18)](#f18)</b>:
#  
# <b id="f19">$$w_{H}=\left(\frac{\xi p_{A}}{\sigma}\right) \left(\frac{pop}{n}+\phi\left(\frac{pop^\ast}{n^\ast}\right)\right) \tag{19}$$</b>
# 
# Respectively, the real profits of entrepreneur in foreign country are:
# 
# <b id="f20">$$w_{H}^{\ast}=\left(\frac{\xi p_{A}}{\sigma}\right) \left(\frac{pop^\ast}{n^\ast}+\phi\left(\frac{pop}{n}\right)\right) \tag{20}$$</b>
# 
# <p style="text-align: justify;">Taking the partial derivatives of equation <b id="a19">[(19)](#f19)</b> with respect to (i) market size (pop), (ii) effective number of firms in the home country $(n)$ and (iii) transport costs $(\tau)$, we observe the following:</p>
# 
# * <p style="text-align: justify;">The higher the population/market size, the higher the real profits of entrepreneur $\to$ home market effect</p>
# 
# * <p style="text-align: justify;">The higher the effective number of firms in the home country, the lower the real profits of entrepreneur $\to$ compete with more firms $\to$ competition effect</p>
# 
# * <p style="text-align: justify;">The higher the transport costs, the less the freeness and the lower the real profits of entrepreneur $\to$ spreading effect </p>
# 
# ### <b id="b12">Utility for entrepreneurs</b>  
# 
# <p style="text-align: justify;">The indirect utility of entrepreneur, which gives his utility given the real profits that he has, is given using equations <b id="a1">[(1)](#f1)</b>, <b id="a4">[(4)](#f4)</b>, <b id="a6">[(6)](#f6)</b>, <b id="a14">[(14)](#f14)</b> and <b id="a19">[(19)](#f19)</b>:</p>
#  
# <b id="f21"> $$V=\left(\frac{\xi}{\sigma} \right) \left(\frac{pop}{n}+\phi \left(\frac{pop^\ast}{n{^\ast}}\right) \right)-\xi+\xi\ln\xi-\ln\left(\frac{\sigma c_{x} w_{L} n^{\frac{1}{(1-\sigma)}}}{(\sigma-1)p_{A}} \right) \tag{21}$$</b>
# 
# The corresponding one for entrepreneur in the foreign country is:
# 
# <b id="f22">$$V^{\ast}=\left(\frac{\xi}{\sigma} \right) \left(\frac{pop^\ast}{n{^\ast}} + \phi\left(\frac{pop}{n} \right)\right)-\xi+\xi\ln\xi-\ln\left(\frac{\sigma c_{x} w_{L} {n^{\ast}}^{\frac{1}{(1-\sigma)}}}{(\sigma-1)p_{A}} \right) \tag{22}$$</b>
# 
# <p style="text-align: justify;">Taking the difference between <b id="a21">[(21)](#f21)</b> and <b id="a22">[(22)](#f22)</b> we can infer in which country the entrepreneurs would want to locate. They will locate in the country which gives them the higher utility.</p>
# 
# <b id="f23"> $$V-V^{\ast}=\left( \frac{\xi}{\sigma-1} \right) \ln\left(\frac{n}{{n^\ast}} \right)+\left(\frac{\xi(1-\phi)}{\sigma} \right) \left(\frac{pop}{n}-\frac{pop^{\ast}}{n^{\ast}} \right) \tag{23}$$</b>
# 
# Another way to express equation <b id="a23">[(23)](#f23)</b> is the following one:
# 
# $$V-V^{\ast}=\left( \frac{\xi}{\sigma-1} \right)\ln\left(\frac{\xi+ \phi(1-h)}{{1-h+\phi h}} \right)+\left(\frac{\xi(1-\phi)}{\sigma} \right) \left(\frac{\rho+h}{h+\phi(1-h)}- \frac{\rho^{\ast}+1-h}{1-h+\phi h} \right) \tag{23'}$$
# 
# 
# <b id="f24">$$V-V^{\ast}=\xi \ln \left(\frac{P^{\ast}}{P} \right)+w_{H}-w^{\ast}_{H} \tag{24}$$</b>
# 
# <p style="text-align: justify;">The first term of equation <b id="a24">[(24)](#f24)</b> captures the consumer/price index effect and the second term captures the profits effect. Furthermore, equation <b id="a23">[(23)](#f23)</b> expresses the relation between the difference of indirect entrepreneur's utility in home and foreign country $V-V^{\ast}$ and the share of entrepreneurs that work in home country $(h)$. Using equations <b id="a23">[(23)](#f23)</b> and <b id="a24">[(24)](#f24)</b> we will answer all the following questions trying also to examine the agglomeration and dispersion effects. Furthermore, we use the same values as the Pflueger’s paper: $\rho=\rho^{\ast}=1, \xi=0.3, \sigma=6$.</p>

# ## <b id="b13">Simulation</b>  
# 
# ### <b id="b14">(i) Higher transport costs multiplier $\pmb{(\tau)}$</b>  
# 
#  <p style="text-align: justify;">Firstly, we plot the equivalent of Figure 1 of Pflueger (2004) based on which we will observe the effects that changes in transport costs provoke.For initial transportation cost multiplier $(\tau)$ we use the value  $\tau=1.4$, which replicates the baseline line in the paper. After that, we increase its value to $\tau=1.5$ which will provide the answer to question (i) and we also decrease its value to $\tau=1.1$ only for the purpose to depict the same graph as the paper does. Therefore, the graph is: </p>

# In[11]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# This inline command allows the plots to show up directly in the notebook
get_ipython().magic(u'matplotlib inline')


# In[12]:

# Since the data is generated by an equation, we don't actually need to import any data, we can recreate the equation
# and generate the input values

# Pandas creates nice dataframes to store values efficiently and neatly
data = pd.DataFrame()
# Generating our h values, the range function stops 1 before the end value, hence here we go to 101 instead of 100
data['h'] = pd.Series([i/100.0 for i in range(0,101)])


# In[13]:

# Just visualizing the top of our newly made data
data.head()


# In[1]:

# Our equation in question
def equation(h, sigma, epsilon, psi, rho, rho_star):
    return epsilon/(sigma-1)*np.log((h+psi-psi*h)/(1-h+psi*h))+((epsilon-epsilon*psi)/sigma)*(((rho+h)/(h+psi-psi*h))-((rho_star+1-h)/(1-h+psi*h)))


# In[18]:

# Creating the figure and sizing it nicely
fig = plt.figure(figsize=(12,6))
plt.grid(True, axis='y', linestyle='-')

# Plotting lines 
plt.plot(data['h'], equation(data['h'],6, 0.3,  0.19, 1, 1), color='blue', linewidth=3, label='Intermediate '+r'$\tau$'+'=1.4')
plt.plot(data['h'] , equation(data['h'],6, 0.3,  0.13, 1, 1), '--', color='red', linewidth=3, label='High '+r'$\tau$'+'=1.5')
plt.plot(data['h'],  equation(data['h'],6, 0.3, 0.62, 1, 1), color='green', linewidth=3, label='Low '+r'$\tau$'+'=0.65')

# Labeling axes and show the legend
plt.ylabel('V-V*',fontweight='bold')
plt.xlabel('h',fontweight='bold')
plt.title('Figure 1: Change in transport costs')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=3)

# Adding in letters where the lines meet the x-axis
plt.text(0.5, 0.006, 'A')
plt.text(0.2, 0.006, 'B')
plt.text(0.8, 0.006, 'C')


#  <p style="text-align: justify;">From figure one, it is obvious that when $\tau=1.4$ there are three equilibria. More specifically, the equilibrium in which the number of entrepreneurs is the same between the two countries is unstable $h=0.5$. The reason for this is: once one entrepreneur moves from home country to foreign country (moves left) then $V-V^{\ast}<0$, which means that the indirect utility is higher in foreign country than in home country and entrepreneur has incentive to deviate. It is beneficial for entrepreneur as a consumer to move to the foreign country as there is more variety of products there (positive relation between $P^{\ast}$ and effective number of firms $n^{\ast}$ using equation <b id="a15">[(15)](#f15)</b>. The same tendency is followed by other entrepreneurs who start to locate in foreign country. However, the more entrepreneurs located in foreign country, the more competition exists and the less their profits (negative relation between $w^{\ast}_{H}$ and $n^{\ast}$.using equation <b id="a20">[(20)](#f20)</b>. Therefore, skilled labour stops to move to foreign country when $h=0.2$ (point B). In this point, there is balance between their profits as consumers and their losses as producers and nobody wants to deviate from it. The same explanation holds for point $h=0.8$, which is also stable (point C).</p>
# 
#  <p style="text-align: justify;">Assuming that the transportation costs increases to level  $\tau=1.5$ then there is only one stable equilibrium equal to $h=0.5$. None entrepreneur wants to deviate neither to home neither to foreign country. In particular, if one entrepreneur moves from home country to foreign then $V-V^{\ast}>0$ which means that the utility in foreign country is lower than in home country. In particular, the entrepreneur is benefited as a consumer because in the foreign country there is higher variety but on the other hand he loses sales because he cannot anymore to serve the unskilled labour in home city which is immobile. His losses outweigh his benefits and therefore it is not beneficial for him to deviate from the equilibrium. The same explanation holds if an entrepreneur moves from foreign to home country.</p>
# 
#  <p style="text-align: justify;">The dynamics that describe the transition between the new and the former equilibrium is as follows: Let us assume that the initial equilibrium is $h=0.8$ ($80\%$ of skilled labour located in home country) which is stable as described above. When $\tau=1.5$, then red dashed-line describes the dynamics in the model. In point $h=0.8$, the value $V-V^{\ast}$ is now negative and entrepreneurs will have incentive to move in the foreign country where the competition is lower and they share the market with less competitors. The explanation behind this tendency is that as freeness of trade decreases (when $\tau$ increases) it becomes more difficult for home entrepreneurs to export in foreign country. So, it is not advantageous for them to agglomerate in home country (negative relation between entrepreneur’s wage and transport costs) even though they benefit from vast variety. Entrepreneurs move to foreign country until their benefits as producers and losses as consumers become equal and this holds at point  $h=0.5$. It can be concluded that transport costs weaken the agglomeration forces and counties are more segregated (complete equality in our example). The corresponding explanation is used to describe the transition between point $h=0.2$ (the old one) and point $h=0.5$ (the new one) in which skilled labour moves form foreign country to home one <b id="a25">[[1]](#f25)</b>. </p>

#  <p style="text-align: justify;">Concerning the real wages of unskilled workers, we know that we have to consider not only their nominal wages which in this model are equal to $1$ as proved earlier, but also the cost of living. This means that the price index/ consumer's basket has to be calculated in both countries. Examining the situation in which there is transition from $h=0.8$ to $h=0.5$, more skilled labour moves to foreign country and as a result its number of effective firms increases ($n^{\ast}$ ). From equations <b id="a14">[(14)](#f14)</b> and <b id="a15">[(15)](#f15)</b>, it is apparent that home’s price index becomes higher (from $0.49$ to $0.53$) and foreign country’s price index becomes lower (from $0.59$ to $0.54$). Given that, the real wage of unskilled labour decreases domestically and increases abroad. A similar argument holds for the transition between $h=0.2$ to $h=0.5$, where the real wage of unskilled labour increases domestically and decreases abroad (home price index decreases from $0.59$ to $0.54$ and foreign price index increases from $0.49$ to $0.53$).</p>

# <p style="text-align: justify;"><p style="text-align: justify;"> <b id="f25">[1]</b>: In order to replicate the paper’s graph we consider the case in which transport cost multiplier decreases to $1.1$. In brief, the green straight line represents now the dynamics of the model and it is clear that the equilibrium $h=0.5$ is not stable. Entrepreneurs have incentive to agglomerate in only one of the countries. They benefit from consumer’s perspective and “crowding in the market” is not so important because the transport costs are really low and therefore they can always export their products to the counterpart country. It can be concluded that when transport costs are low, then there are not significant counterforces against agglomeration forces.</p>

# ### <b id="b15">(ii) Stronger taste for variety (lower $\pmb{\sigma}$)</b>
# 
# <p style="text-align: justify;">In order to replicate how changes in elasticity of substitution $(\sigma)$ affect the agglomeration and dispersion forces we use as baseline the value $\sigma=6$. Afterwards, we increase taste "for variety" through decreasing $\sigma $ to levels $4$ and $2.55$. In all cases, there are three equilibria, two of them are stable and the last one is unstable. When σ decreases, the agglomeration also increases in one of the two cities. The corresponding graph is: </p>

# In[22]:

# Creating the figure and sizing it to resemble original graphs
fig = plt.figure(figsize=(12,6))
plt.grid(True, axis='y', linestyle='-')

# Plotting lines with 
plt.plot(data['h'], equation(data['h'],6, 0.3,  0.185934432, 1, 1), color='blue', linewidth=3, label='baseline '+r'$\sigma$'+'=6')
plt.plot(data['h'] , equation(data['h'],4, 0.3,  0.185934432, 1, 1), '--', color='red', linewidth=3, label='lower '+r'$\sigma$'+'=4')
plt.plot(data['h'],  equation(data['h'],2.55, 0.3,  0.185934432, 1, 1), color='green', linewidth=3, label='lower '+r'$\sigma$'+'=2.55')

# Labeling axes and show the legend
plt.ylabel('V-V*',fontweight='bold')
plt.xlabel('h',fontweight='bold')
plt.title('Figure 2: Change in elasticity of substitution')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=3)

# Adding in letters where the lines meet the x-axis
plt.text(0.5, 0.006, 'A')
plt.text(0.2, 0.006, 'B')
plt.text(0.1, 0.001, 'C')
plt.text(0.01, 0.001, 'D')
plt.text(0.8, 0.002, 'E')
plt.text(0.9, 0.001, 'F')
plt.text(0.98, 0.006, 'H')


# <p style="text-align: justify;">Assuming that the economy is at point B $(h=0.2)$ which is stable as has been described in question (i) and so $80\%$ of skilled labor located in foreign country and $20\%$ in home country. Then, there is a shock in the economy and consumers increase their taste for variety $(\sigma=4)$, meaning that they prefer to have more manufacturing goods at their disposal. Therefore, dynamics of the model are now described by the red dashed-line. The transition to the new equilibrium is as follows: </p>
# 
# <p style="text-align: justify;">At point B, after the shock,  $V-V^{\ast}$ becomes negative indicating that the indirect utility of entrepreneur is higher in foreign country than home country. As a result, the latter would have incentive to deviate from point B and move to foreign country (towards point C). As "preference for higher variety in products" increases, entrepreneurs prefer to move to foreign country where there is already higher variety than home country (more effective firms abroad). Price index decreases abroad (from $0.5$ to $0.29$). Entrepreneurs value consumer’s benefits more than profit losses and that is why economy moves towards point C $(h=0.11)$. While the latter gather in foreign country, competition rises and their profits decrease. The transition stops at point C where the consumer’s benefit in foreign country equal to producer’s cost. None wants to deviate from it. A similar reasoning can be given in order to explain the transition from point E to point F $(h=0.89)$.</p>
# 
# <p style="text-align: justify;">In conclusion, higher taste for variety enhances agglomeration forces and weakens dispersion forces as the consumer/ price index effect (first term in right side of equation (<b id="a24">[(24)](#f24)</b>outweigh profits effect ((second term in right side of equation <b id="a">[(24)](#f)</b>). In the extreme case in which $\sigma=2.55$ we observe that all entrepreneurs move to one of the two countries (complete specialization).</p>
# 
# <p style="text-align: justify;">Concerning the real wages of unskilled labour, again we have to examine how changes in $\sigma$ affect the price index in both countries. Examining the situation in which there is transition from $h=0.2$ to $h=0.11$, more skilled labour moves to foreign country and as a result its number of effective firms increases. Using simulation, we observed that as economy moves from point B to point C (decrease in $\sigma$), price index for both countries decreases (this happens because of the specific parameters that we have chosen to do the simulation. It is possible that the price index for the home country increases as less effective firms exist there but for the foreign country the price index always decrease as more effective firms locate there).This means that consumers (skilled and unskilled labor) care a lot about differentiated goods. Consequently, real wages for unskilled workers increases in both countries (with the specific parameters that we used). Furthermore, for even higher taste for variety (even lower values of $\sigma$), the lower the prices indexes and the higher the real wages of $L$ and $L^{\ast}$. The same argumentation holds for the transition from point E to point F, in which price indexes also decrease resulting to higher real wages for unskilled labour.</p>
# 

# ### <b id="b16">(iii) Smaller share of immobile people</b>  
# 
# <p style="text-align: justify;">In order to replicate how the share of immobile workers relative to the whole population $\left( \gamma=\frac{L+L^{\ast}}{POP+POP^{\ast}} \right)$ affects the agglomeration and dispersion forces we use as baseline the values $\rho=\rho^{\ast}=1$ as Pflueger assumes Afterwards, there is a shock in economy which decreases γ and as a result the share of unskilled labour in both regions ($\rho$ and $\rho^{\ast}$).</p>
# 
# $$\gamma=\frac{L+L^{\ast}}{POP+POP^{\ast}}=\frac{L+L^{\ast}}{L+L^{\ast}+\overline{H}}=\frac{\rho \overline{H}+\rho^{\ast}\overline{H}}{\rho \overline{H}+\rho^{\ast}\overline{H}+\overline{H}}=\frac{\rho+\rho^{\ast}}{\rho+\rho^{\ast}+1}$$
# 
# <p style="text-align: justify;">So, the latter parameters decrease to values $\rho=\rho^{\ast}=0.8$ (this two parameters are assumed to be always equal). In both cases (before and after the shock), there are three equilibria, two of them are stable and the last one in unstable. When $\rho$ and $\rho^{\ast}$ the agglomeration also increases in one of the two cities. The corresponding graph is:</p>

# In[21]:

# Creating the figure and sizing it to resemble original graphs
fig = plt.figure(figsize=(12,6))
plt.grid(True, axis='y', linestyle='-')

# Plotting lines with 
plt.plot(data['h'], equation(data['h'],6, 0.3,  0.185934432, 1, 1), color='blue', linewidth=3, label='baseline '+r'$\rho = \rho*$'+'=1')
plt.plot(data['h'] , equation(data['h'],6, 0.3, 0.185934432, 0.8, 0.8), '--', color='red', linewidth=3, label='lower '+r'$\rho = \rho*$'+'=0.8')
plt.plot(data['h'],  equation(data['h'],6, 0.3, 0.185934432, 0.6, 0.6), color='green', linewidth=3, label='lower '+r'$\rho = \rho*$'+'=0.6')

# Labeling axes and show the legend
plt.ylabel('V-V*',fontweight='bold')
plt.xlabel('h',fontweight='bold')
plt.title('Figure 3: Change in total immobile labor')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=3)

# Adding in letters where the lines meet the x-axis
plt.text(0.5, 0.003, 'A')
plt.text(0.2, 0.003, 'B')
plt.text(0.8, 0.003, 'C')


# <p style="text-align: justify;">Let us assume that the economy is at point B which is stable as proved in question (i). After the shock (decrease in $\rho$ and $\rho^{\ast}$ economy is described by the red dashed-line. More specifically, after the shock, the transition to the new equilibrium is as follows:</p>
# 
# <p style="text-align: justify;">At point B, after the shock $V-V^{\ast}$ becomes negative indicating that the indirect utility of entrepreneurs is higher in foreign country than home country because of the fact that the profits in foreign country are higher than in home country. As a result, the latter would have incentive to deviate from point B and move to foreign country. From equation <b id="a24">[(24)](#f24)</b>, it is obvious that changes in $\rho$ and $\rho^{\ast}$ affect only the term $w_{H}-w_{H}^\ast$, which has to be negative in order that the condition $V-V^{\ast}<0$ holds as we observe in the graph. Skilled labour keeps moving to foreign country until point D where profits between two countries are again the same and no one has incentive to deviate. On the other hand, when economy moves from point C to point E, the corresponding condition that must be hold is $w_{H}-w_{H}^\ast>0$. From the above analysis it is clear when $\rho$ and $\rho^{\ast}$ change then profits effect (second term in equation <b id="a24">[24](#f24)</b>) dominates while price effect (first term in equation <b id="a24">[24](#f24)</b>) does not play any role in the transition of the economy.</p>

# ## <b id="b17">Conclusion</b>    
# 
# <p style="text-align: justify;">In Pfueger's paper we distinguish two basic fundamental forces. Fisrt of all, there are agglomeration forces which can be created through benefits from variety or through the home market effect. More specifically, the higher the variety of manufacturing firms in one city the lower the consumer's basket and consequently the more intensive the tendecy of firms to be established there (as entrepreneurs are also consumers who benefit from low price index). According to home market effect, companies have the insentive to agglomerate in cities in which there are many immobile-unskilled workers and at the same time there are few competitive firms. Expect for agglomeration forces there are also dispersion forces. The main reason why these forces emerge is the existence of transport costs that prevent all firms to be located in the same place. In particular, transpport costs make difficult for companies to export to other regions. The above mentioned forces contibute to the fact that in the real world there is neither complete specialisation (one city takes all the innovative production activity) nor complete equality (all cities have equal number of companies). The truth lies somewhere in between and that is why there are not only large cities but also small ones. In the cases that we examined, it is obvious that higher transport costs weaken agglomeration forces while factors as higher taste for manufacturing goods or smaller share of unskilled labor in one region enhance agglomeration forces.</p>

# ### <b id="b18">Appendix</b>  

# Notation| Interpretation| Value of Parameters|
# :-------------: | :-------------: | :-------------:
# $\sigma$ | Elasticity of substitution between manufacturing goods | $6$
# $\xi$ | Preference for manufactured goods/size of the market |  $0.3$
# $c_{x}$ | Production cost for one unit of manufacturing good |  $1$
# $N$ | Skilled Labour in region | 
# $L$ | Unskilled Labour in region |
# $w_{H}$ | Wage of skilled labour (profits of the firms they run) |
# $w_{L}$ | Wage of unskilled labour |
# $C_{A}$ | Consumption of agricultural goods |
# $C_{X}$ | Consumption of manufactured goods |
# $P_{A}$ | Price of agricultural goods | $1$
# $\ast$ | Asterisk denotes "foreign" region (no asterisk denotes home) |
# $Pop=(\rho+h)\overline{H}$ | Population size in the region |
# $h=\frac{N}{N+N^{\ast}}=\frac{N}{\overline{H}}$ | Share of total skilled labour supply that works in home country |
# $p=\displaystyle \frac{L}{N+N^{\ast}}$ | Unskilled labour in home region out of total number of skilled labour | $1$
# $n=N+N^{\ast} \tau^{1-\sigma}=\overline{H}(h+\phi(1-h))$ | Effective number of firms in home region |
# $\phi=\tau^{1-\sigma}$ | Freeness of trade | $0.19$ 
# $\tau$ | Transport costs | $1.4$
# $\overline{H}$ | Total number of entrepreneurs | $100$
