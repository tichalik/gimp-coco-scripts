def import_coco(filename, i_id):
    import json
    #---------------------------open COCO file--------------------------- 
    file = open(filename)
    jsonfile = json.load(file)
    file.close()
    #---------------------------get label names---------------------------
    labels = {}
    for l in jsonfile["categories"]:
        labels[str(l["id"])] = l["name"]
    #---------------------------annotations to paths---------------------------
    for path in jsonfile["annotations"]:
        if (path["image_id"] == i_id):
            #---------------------------copy points---------------------------
            path_str = '<path d="'
            for segment in path["segmentation"]:
                #the path must start "M x,y" which defines the starting point
                #in this case it's the first vertex 
                path_str += " M " + str(segment[0]) + ", "+str(segment[1])
                #adding more vertices
                i = 0;
                while(i<len(segment)):
                    path_str += " L " +str(segment[i]) +"," + str(segment[i+1])
                    i += 2
                #close the path
                path_str += " Z "
            path_str += """ "/>"""
            #---------------------------add path to picture---------------------------
            num, _ = pdb.gimp_vectors_import_from_string(gimp.image_list()[0], path_str, -1, False, False)
            #---------------------------rename added paths---------------------------
            for i in range(num):
                gimp.image_list()[0].vectors[i].name = str(path["category_id"]) + " " + labels[path["category_id"]] + str(i)