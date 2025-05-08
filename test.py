from reader import getText
from chunking import semanticChunking
from vectorization import vectorization

text = getText('documents\\ТУ 24.33.20-038-75483238-2017 с изм 1-20..docx')


chunks = semanticChunking(text)

vect = vectorization(chunks)

# for i, chunk in enumerate(chunks):
#     print(f'Фрагмент: {i + 1} \n {chunk}')

print(f'NUMDATA: {len(vect)} \n Feature: {len(vect[0])}')
