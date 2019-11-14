# import collections
# import math


# def lcs(str1, str2):
#     cached = collections.defaultdict(dict)
#     tokens1, tokens2 = str1.split(), str2.split()

#     for i in range(-1, len(tokens1)):
#         for j in range(-1, len(tokens2)):

#             if i == -1 or j == -1:
#                 cached[i][j] = [[]]

#             else:
#                 if tokens1[i] == tokens2[j]:
#                     out = [x + [(tokens1[i], j)] for x in cached[i - 1][j - 1]]

#                 else:
#                     a, b = cached[i - 1][j], cached[i][j - 1]

#                     if len(a[0]) == len(b[0]):
#                         out = a + b if a[len(a) - 1] != b[len(b) - 1] else a
#                     else:
#                         out = a if len(a[0]) > len(b[0]) else b

#                 cached[i][j] = out

#     return cached[len(tokens1) - 1][len(tokens2) - 1]

# def seq_contiguity(subseqs):
#     score = 0
    
#     for subseq in subseqs:
#         seq = [y for x, y in subseq]
#         val, ent = 1, 0.
    
#         for idx in range(1, len(seq)):
#             if seq[idx] == seq[idx - 1] + 1:
#                 val += 1
#             else:
#                 ent += val * math.log(val)
#                 val = 1
#         ent += val * math.log(val)
#         score = max(score, ent)
#     return score

# S1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ligula lectus, hendrerit quis leo at, efficitur commodo erat. Etiam vitae nulla quis dolor sollicitudin luctus. Cras blandit pulvinar auctor. In semper tellus sit amet pretium vehicula. Proin quis elementum sem. Maecenas est diam, hendrerit eu elementum ut, ullamcorper ut massa. Integer turpis mi, semper consequat orci ac, auctor semper est. Donec commodo auctor lorem mollis imperdiet. Morbi a facilisis nulla, ac mattis velit. Aliquam efficitur eleifend iaculis. Vivamus mollis lobortis leo, vel feugiat nunc venenatis ac. Quisque vel tempor magna. Nunc convallis felis ultricies blandit condimentum. In consequat scelerisque ante id maximus. Quisque fermentum vel eros sed ullamcorper. Mauris laoreet porta ligula sed feugiat. Sed quis mi convallis, vehicula lorem nec, consequat neque. Proin aliquet pellentesque nisl eget dapibus. In non quam sit amet orci porttitor sodales. Duis vulputate nibh tempus lacus lacinia ornare. Pellentesque feugiat nulla a nisl bibendum, et rhoncus elit dapibus. Duis vitae velit id sapien efficitur mollis non sed odio. Aliquam elementum luctus augue. Proin facilisis ut ipsum pulvinar sodales. Morbi vitae rhoncus tortor. Suspendisse aliquam tortor sed dui elementum placerat. Fusce odio lectus, tempus nec lorem et, pretium cursus quam. Aenean tempus ipsum dui, a tincidunt erat posuere a. Mauris venenatis elit eget justo maximus semper. Donec sagittis urna dui, vitae semper mauris cursus vitae. Quisque rutrum enim egestas massa tincidunt porttitor eu vitae augue. Nam pellentesque viverra velit ut iaculis. Praesent pulvinar, arcu et sollicitudin pellentesque, dui ipsum lobortis libero, at tincidunt justo leo sollicitudin ante. Etiam eleifend gravida nisl sed lacinia. In pulvinar mauris sed aliquam porta. Nunc rhoncus erat nec sem hendrerit aliquet. In hac habitasse platea dictumst. Donec magna ex, facilisis non dui sed, tempus semper est. Suspendisse non sapien massa. Vestibulum eros dolor, pharetra eget mi ultrices, luctus pulvinar enim. Aliquam dictum elit ut tellus bibendum, sit amet aliquam quam ultrices. Proin mattis ac eros id mollis. Vestibulum sit amet bibendum urna. Nulla sit amet ex a sem placerat condimentum. Nulla ligula mauris, scelerisque non consectetur ut, eleifend ut neque. Proin a molestie justo. Nullam et erat finibus, luctus ligula id, porta odio. Duis ac nisl quis urna interdum fringilla. Vestibulum erat mi, placerat sed convallis vitae, iaculis at nisl. Vivamus id justo ultricies, hendrerit dui sed, elementum ante. Ut luctus efficitur lectus, at consectetur urna commodo eget. Nunc at pretium quam, non mattis turpis."
# S2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ligula lectus, hendrerit quis leo at, efficitur commodo erat. Proin quis elementum sem. Maecenas est diam, hendrerit eu elementum ut, ullamcorper ut massa. Integer turpis mi, semper consequat orci ac, auctor semper est. Donec commodo auctor lorem mollis imperdiet. Morbi a facilisis nulla, ac mattis velit. Aliquam efficitur eleifend iaculis. Vivamus mollis lobortis leo, vel feugiat nunc venenatis ac. Quisque vel tempor magna."

# print(lcs(S1,S2))




import collections
def lcs(s1, s2):
    tokens1, tokens2 = s1.split(), s2.split()
    cache = collections.defaultdict(dict)
    for i in range(-1, len(tokens1)):
        for j in range(-1, len(tokens2)):
            if i == -1 or j == -1:
                cache[i][j] = 0
            else:
                if tokens1[i] == tokens2[j]:
                    cache[i][j] = cache[i - 1][j - 1] + 1
                else:
                    #Devuelve el elemento más grande
                    cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    return cache[len(tokens1) - 1][len(tokens2) - 1]
s1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ligula lectus, hendrerit quis leo at, efficitur commodo erat. Etiam vitae nulla quis dolor sollicitudin luctus. Cras blandit pulvinar auctor. In semper tellus sit amet pretium vehicula. Proin quis elementum sem. Maecenas est diam, hendrerit eu elementum ut, ullamcorper ut massa. Integer turpis mi, semper consequat orci ac, auctor semper est. Donec commodo auctor lorem mollis imperdiet. Morbi a facilisis nulla, ac mattis velit. Aliquam efficitur eleifend iaculis. Vivamus mollis lobortis leo, vel feugiat nunc venenatis ac. Quisque vel tempor magna. Nunc convallis felis ultricies blandit condimentum. In consequat scelerisque ante id maximus. Quisque fermentum vel eros sed ullamcorper. Mauris laoreet porta ligula sed feugiat. Sed quis mi convallis, vehicula lorem nec, consequat neque. Proin aliquet pellentesque nisl eget dapibus. In non quam sit amet orci porttitor sodales. Duis vulputate nibh tempus lacus lacinia ornare. Pellentesque feugiat nulla a nisl bibendum, et rhoncus elit dapibus. Duis vitae velit id sapien efficitur mollis non sed odio. Aliquam elementum luctus augue. Proin facilisis ut ipsum pulvinar sodales. Morbi vitae rhoncus tortor. Suspendisse aliquam tortor sed dui elementum placerat. Fusce odio lectus, tempus nec lorem et, pretium cursus quam. Aenean tempus ipsum dui, a tincidunt erat posuere a. Mauris venenatis elit eget justo maximus semper. Donec sagittis urna dui, vitae semper mauris cursus vitae. Quisque rutrum enim egestas massa tincidunt porttitor eu vitae augue. Nam pellentesque viverra velit ut iaculis. Praesent pulvinar, arcu et sollicitudin pellentesque, dui ipsum lobortis libero, at tincidunt justo leo sollicitudin ante. Etiam eleifend gravida nisl sed lacinia. In pulvinar mauris sed aliquam porta. Nunc rhoncus erat nec sem hendrerit aliquet. In hac habitasse platea dictumst. Donec magna ex, facilisis non dui sed, tempus semper est. Suspendisse non sapien massa. Vestibulum eros dolor, pharetra eget mi ultrices, luctus pulvinar enim. Aliquam dictum elit ut tellus bibendum, sit amet aliquam quam ultrices. Proin mattis ac eros id mollis. Vestibulum sit amet bibendum urna. Nulla sit amet ex a sem placerat condimentum. Nulla ligula mauris, scelerisque non consectetur ut, eleifend ut neque. Proin a molestie justo. Nullam et erat finibus, luctus ligula id, porta odio. Duis ac nisl quis urna interdum fringilla. Vestibulum erat mi, placerat sed convallis vitae, iaculis at nisl. Vivamus id justo ultricies, hendrerit dui sed, elementum ante. Ut luctus efficitur lectus, at consectetur urna commodo eget. Nunc at pretium quam, non mattis turpis."
s2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ligula lectus, hendrerit quis leo at, efficitur commodo erat. Proin quis elementum sem. Maecenas est diam, hendrerit eu elementum ut, ullamcorper ut massa. Integer turpis mi, semper consequat orci ac, auctor semper est. Donec commodo auctor lorem mollis imperdiet. Morbi a facilisis nulla, ac mattis velit. Aliquam efficitur eleifend iaculis. Vivamus mollis lobortis leo, vel feugiat nunc venenatis ac. Quisque vel tempor magna."
original = len(s1.split())
copia = lcs(s1,s2)
print("El número de palabras similares son: ",copia)


porcentaje = float((copia*100)/original)

print("El porcentaje de plagio es: ",round(porcentaje,2), "%")