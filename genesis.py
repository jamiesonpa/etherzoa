import random


def generate_promoter():
    bases = ["A","T","A","T","G","C","G","C","G","C","G","C"]
    gorc = ["G","C"]
    length = random.randrange(100,1000)
    counter = 0
    promoter = ""
    while counter < length:
        promoter = promoter + random.choice(bases)
        counter +=1
    promoter.replace("TATAA", "GGGGG")
    promoter = promoter.replace("TATAA","CG")
    promoter = promoter.replace("TATAT", "CG")
    promoter = promoter.replace("TTTAA","CG")
    promoter = promoter.replace("AATAA","CG")
    promoter = promoter.replace("TAAAA","CG")
    promoter = promoter.replace("AATAA","CG")
    promoter = promoter.replace("ATG","CG")
    promoter = promoter + random.choice(gorc) + random.choice(gorc) + random.choice(gorc) + random.choice(gorc) + random.choice(gorc) + random.choice(gorc) + random.choice(gorc) + "TATAA"
    critical_bases = []
    number_of_critical_bases = random.randrange(10,20)
    critbase_counter = 0
    while critbase_counter < number_of_critical_bases:
        critbase_position = random.randrange(10,len(promoter)-1)
        critical_bases.append(critbase_position)    
        critbase_counter += 1
    
    positive_bases = {}
    for critical_base in critical_bases:
        positive_bases[critical_base] = promoter[critical_base]
    
    negative_bases = {}
    for critical_base in critical_bases:
        if promoter[critical_base] == "A":
            negative_bases[critical_base] = "T"
        elif promoter[critical_base] == "T":
            negative_bases[critical_base] = "A"
        elif promoter[critical_base] == "G":
            negative_bases[critical_base] = "C"
        else:
            negative_bases[critical_base] = "G"

    retval = [promoter, positive_bases, negative_bases]
    return retval

def generate_gene():
    gene = ""
    length = random.randrange(400,4000)
    bases = ["A","T","A","T","A","T","G","C"]
    gorc = ["G","C"]
    counter = 0
    while counter < length:
        gene = gene + random.choice(bases)
        counter +=1
    stop_codons = ["TAA","TAG","TGA"]
    gene = gene.replace("TATAA","CG")
    gene = gene.replace("TATAT", "CG")
    gene = gene.replace("TTTAA","CG")
    gene = gene.replace("AATAA","CG")
    gene = gene.replace("TAAAA","CG")
    gene = gene.replace("AATAA","CG")
    gene = gene.replace("ATG","CG")
    gene = gene.replace("TAA","CG")
    gene = gene.replace("TAG","CG")
    gene = gene.replace("TAG","CG")
    gene = gene.replace("ATG","CG")
    gene = random.choice(gorc) + random.choice(gorc) + random.choice(gorc) + random.choice(gorc) + "ATG" + gene
    gene = gene + random.choice(stop_codons)

    critical_bases = []
    number_of_critical_bases = random.randrange(10,20)
    critbase_counter = 0
    while critbase_counter < number_of_critical_bases:
        critbase_position = random.randrange(0,len(gene)-1)
        critical_bases.append(critbase_position)    
        critbase_counter += 1
    
    positive_bases = {}
    for critical_base in critical_bases:
        positive_bases[critical_base] = gene[critical_base]
    
    negative_bases = {}
    for critical_base in critical_bases:
        if gene[critical_base] == "A":
            negative_bases[critical_base] = "T"
        elif gene[critical_base] == "T":
            negative_bases[critical_base] = "A"
        elif gene[critical_base] == "G":
            negative_bases[critical_base] = "C"
        else:
            negative_bases[critical_base] = "G"

    retval = [gene, positive_bases, negative_bases]
    return retval

def generate_intergene_sequence():
    bases = ["A","T","G", "C"]
    length = random.randrange(20,200)
    counter = 0
    igs = ""
    while counter < length:
        igs = igs + random.choice(bases)
        counter += 1
    igs = igs.replace("TATAA", "GC")
    igs = igs.replace("TATAT", "GC")
    igs = igs.replace("TTTAA","GC")
    igs = igs.replace("AATAA","GC")
    igs = igs.replace("TAAAA","GC")
    igs = igs.replace("AATAA","GC")
    igs = igs.replace("ATG","GC")
    return igs

def generate_organism_base():
    genes = ["gene1", "gene2","gene3","gene4","gene5","gene6","gene7","gene8","gene9","gene10"]

    organism = {}

    for gene in genes:
        gene_values = {}
        gene_values["promoter_value"] = 1
        promoter_information = generate_promoter()
        gene_values["promoter"] = promoter_information[0]
        gene_values["positive_promoter_bases"] = promoter_information[1]
        gene_values["negative_promoter_bases"] = promoter_information[2]
        increment = 1/len(gene_values["positive_promoter_bases"].keys())
        bases_to_change = random.randint(0,len(gene_values["positive_promoter_bases"].keys()))
        change_base_counter = 0
        while change_base_counter < bases_to_change:
            base_to_change = random.choice(list(gene_values["positive_promoter_bases"].keys()))
            current_promoter = gene_values["promoter"]
            temp_promoter = list(gene_values["promoter"])
            temp_promoter[base_to_change] = gene_values["negative_promoter_bases"][base_to_change]
            new_promoter = "".join(temp_promoter)
            gene_values["promoter"] = new_promoter
            change_base_counter +=1
        
        counter = 0
        running_value = 0
        for base in list(gene_values["promoter"]):
            for critbase in gene_values["negative_promoter_bases"].keys():
                if counter == critbase:
                    if base == gene_values["negative_promoter_bases"][critbase]:
                        running_value = running_value - increment
                    elif base == gene_values["positive_promoter_bases"][critbase]:
                        running_value = running_value + increment
                    else:
                        print("couldn't find base in promoter")
            counter +=1
        
        gene_values["promoter_value"] = running_value


        gene_information = generate_gene()
        gene_values["gene_value"] = 1
        gene_values["gene"] = gene_information[0]
        gene_values["positive_gene_bases"] = gene_information[1]
        gene_values["negative_gene_bases"] = gene_information[2]

        increment = 1/len(gene_values["positive_gene_bases"].keys())
        bases_to_change = random.randint(0,len(gene_values["positive_gene_bases"].keys()))
        change_base_counter = 0
        while change_base_counter < bases_to_change:
            base_to_change = random.choice(list(gene_values["positive_gene_bases"].keys()))
            current_gene = gene_values["gene"]
            temp_gene= list(gene_values["gene"])
            temp_gene[base_to_change] = gene_values["negative_gene_bases"][base_to_change]
            new_gene = "".join(temp_gene)
            gene_values["gene"] = new_gene
            change_base_counter +=1

        counter = 0
        running_value = 0
        for base in list(gene_values["gene"]):
            for critbase in gene_values["negative_gene_bases"].keys():
                if counter == critbase:
                    if base == gene_values["negative_gene_bases"][critbase]:
                        running_value = running_value - increment
                    elif base == gene_values["positive_gene_bases"][critbase]:
                        running_value = running_value + increment
                    else:
                        print("couldn't find base in gene")
            counter +=1
        
        gene_values["gene_value"] = running_value
        gene_values["total_value"] = (gene_values["gene_value"] + gene_values["promoter_value"])/2
        organism[gene] = gene_values

    genome = ""
    for key in organism.keys():
        gene = organism[key]["gene"]
        promoter = organism[key]["promoter"]
        genome = genome + str(generate_intergene_sequence())
        genome = genome + promoter + gene
        
    genome = genome.strip().replace("\n","")
    organism["genome"] = genome

    with open("genome.txt", "w+") as writefile:
        writefile.write(organism["genome"])
    # for key in organism.keys():
        # print(str(key) + ": "+ str(organism[key]))

base_organism = generate_organism_base()

# generate_new_organisms(base_organism)
