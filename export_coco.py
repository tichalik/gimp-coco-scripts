def export_coco(output_dir, i_id):
    import json
    annotations = []
    for path in gimp.image_list()[0].vectors:
        s_id = 1
        xmin = path.strokes[0].points[0][0]
        ymin = path.strokes[0].points[0][0]
        xmax = path.strokes[0].points[0][0]
        ymax = path.strokes[0].points[0][0]
        segmentation = []
        for stroke in path.strokes:
            x_points = []
            y_points = []
            points = [ stroke.points[0][i] for i in range(len(stroke.points[0])) if i%6 == 1 or i%6 == 0]
            segmentation.append(points)
            count = 0
            for point in stroke.points[0]:
                if count % 6 == 0:
                    x_points.append(point)
                elif count % 6 == 1: 
                    y_points.append(point)
                count += 1
            if (xmin > min(x_points)):
                    xmin = min(x_points)
            if (xmax < max(x_points)):
                    xmin = max(x_points)
            if (ymin > min(y_points)):
                    ymin = min(y_points)
            if (ymax < max(y_points)):
                    ymax = max(y_points)
        result = { "id":s_id, 
            "image_id":i_id, 
            "category_id": int(path.name.split()[0]), 
            "b_box": [xmin,ymin,xmax, ymax],
            "area": abs((xmax-xmin)*(ymax-ymin)),
            "segmentation" : segmentation,
            "iscrowd": 0
            }
        annotations.append(result)
    file = open(output_dir+"/image"+str(i_id) + ".json", "w")
    file.write(json.dumps( {"annotations":annotations}))
    file.close()		