"""
Author: Zach Stoebner
Created on: 8-6-2019
Descrip: 

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid

"""

#know that input is a list and given cardinality
#know that any contradiction to transivity is invalid
def ruleCheck(rules=[]):

    north_south_relations = set() #ordered tuples s.t. first is north of second
    east_west_relations = set() #ordered tuples s.t. first is east of second

    #creating sets of relations
    for rule in rules:
        split_rule = rule.split(' ')
        if split_rule[1][0] == 'N':
            north_south_relations.add((split_rule[0],split_rule[-1]))
        if split_rule[1][0] == 'S':
            north_south_relations.add((split_rule[-1],split_rule[0]))
        if split_rule[1] == 'E' or (len(split_rule[1]) == 2 and split_rule[1][1] == 'E'):
            east_west_relations.add((split_rule[0],split_rule[-1]))
        if split_rule[1] == 'W' or (len(split_rule[1]) == 2 and split_rule[1][1] == 'W'):
            east_west_relations.add((split_rule[-1],split_rule[0]))

    #function to check transitivity
    def checkTransitive(relations=set()):

        #set of all relations given transitivity
        full_transitive_set = relations.copy()

        hadRelations = True
        while hadRelations:

            #assuming no transitives are found
            hadRelations = False

            #transitives found in current iteration
            transitives = set([(a,d) for a,b in full_transitive_set for c,d in full_transitive_set if b==c])
            if len(transitives) > 0:
                for x,y in transitives:
                    #if contradiction, early stop
                    if (y,x) in full_transitive_set or (y,x) in transitives:
                        return False
                    #if new transitive, add and change hadRelations flag
                    elif (x,y) not in full_transitive_set:
                        full_transitive_set.add((x,y))
                        hadRelations = True

        for rel in full_transitive_set:
            if rel[::-1] in full_transitive_set:
                return False

        return True


    return (checkTransitive(north_south_relations) and checkTransitive(east_west_relations))

#Test rules
rules1 = ["A N B","B NE C","C N A"]
rules2 = ["A NW B", "A N B"]
rules3 = ["A W B","B E C", "A W C"]
rules4 = ["A NW B", "B NE C", "D W B", "F N G","B E D", "F S G"]
print("Valid rules?",ruleCheck(rules4))
