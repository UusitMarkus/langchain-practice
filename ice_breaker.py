from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

information = """Antti Petteri Orpo (s. 3. marraskuuta 1969 Köyliö)[2] on suomalainen poliitikko ja Suomen pääministeri vuodesta 2023. Orpo on ollut Kansallisen Kokoomuksen puheenjohtaja vuodesta 2016.[3]

Hän on toiminut kansanedustajana vuodesta 2007. Huhtikuusta kesäkuuhun 2023 hän toimi väliaikaisena eduskunnan puhemiehenä. Aiemmin Orpo oli Stubbin hallituksen maa- ja metsätalousministeri 2014–2015 sekä Sipilän hallituksen sisäministeri 2015–2016 ja valtiovarainministeri 2016–2019. Vuosina 2012–2014 Orpo toimi kokoomuksen eduskuntaryhmän puheenjohtajana.

Orpo valmistui ylioppilaaksi Säkylän seudun lukiosta vuonna 1989. Hän aloitti opinnot Turun yliopistossa vuonna 1990, ja valmistui valtiotieteiden maisteriksi 12 vuotta kestäneiden opintojensa jälkeen vuonna 2002.[4][5] Hänen pääaineensa oli taloustiede ja pro gradu -tutkielmansa hän teki aiheesta ”Kuntien palvelutuotannon perusteet ja sen uudelleen järjestäminen.”[6][7]

Opiskeluaikanaan Orpo toimi Turun yliopiston ylioppilaskunnan (TYY) pääsihteerinä vuosina 1994–1996 sekä Suomen ylioppilaskuntien liitto SYL:n pääsihteerinä vuosina 1997–1998. Tämän jälkeen hän työskenteli Varsinais-Suomen Kokoomuksen toiminnanjohtajana vuoteen 2001 ja sisäasiainministeri Ville Itälän erityisavustajana 2002–2003. Ennen valintaansa kansanedustajaksi Orpo työskenteli Turun Aikuiskoulutuskeskuksen yrityspalvelujohtajana vuosina 2005–2007.[2]

Poliittinen toiminta
Kunnallispoliitikkona
Kunnallispolitiikassa Orpo on toiminut Turun kaupunginvaltuuston jäsenenä vuosina 1996–2000 ja uudelleen vuodesta 2005. Vuosina 1999–2002 ja 2005–2007 hän oli myös Turun kaupunginhallituksen jäsen, mutta erosi tehtävästä aloittaessaan kansanedustajana. Orpo oli vuosina 2012–2014 Varsinais-Suomen liiton maakuntahallituksen puheenjohtaja. Orpo on ollut myös Varsinais-Suomen kokoomuksen puheenjohtaja vuosina 2005–2012.[2]
"""

if __name__ == "__main__":
    print("Hello LangChain!")
    load_dotenv()
    summary_template = """
    given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
"""

summary_prompt_template = PromptTemplate(
    input_variable="information", template=summary_template
    )

llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

chain = summary_prompt_template | llm
res = chain.invoke(input={"information": information})

print(res)