# GIMP scripts for working with coco.json

Annotating things can be a hard work, but there are programs that make it easier -- for example GIMP. Use these scripts to facillitate your workflow. Unfortunately my knowledge of GIMP API is a bit limited, so the solutions may come as clunky at some times, but they're better than nothing

## usage

In GIMP  open `Filters > Python-Fu > Console` and paste contents of file of your choice. Now the function can be called in normal python way.

### `export_coco(path, image_id)`

exports path of current image into COCO `annotations` proerty, which then can be manually pasted into the rest of COCO json. The `category_id` label is decided by the number at the beginning of the path name 
    
    `path` the output directory
    `image_id` number to use for the `image_id` property
    
### `import_coco(path, image_id)`

import annotations as GIMP paths into current image. The path gets name \[category id] \[category name] \[number] 

    `path` path to json file
    `image_id` which image to import
    
    
## limitations
 - originally done for COCO polygons, not sure how will work with other shapes
 - can only work with one file open in GIMP
 - something strange goes on with the bbox, if it is important to your project, please check the code (and please notify me if you know how to fix it)
 - due to nature of COCO polygons all curves will be interpreted as straight lines
 
# working with GIMP for nongimpers

GIMP may seem intimidating to some, but using raster graphics and an appropriate editor can save you hours of tenous work. Here are some tips, how to use the software:
 - raster to COCO -- these scripts represent COCO annotations as GIMP paths and turning a rater area into polygon outline is easy -- select the area (Select By Color Tool/Fuzzy Select) go `Select > To Path`
 - open path window -- go `Windows > Dockable Windows > Path`
 - path to selection -- click on path in the path window `> To Selection`
 - working on layers -- create new with `ctrl + shift + n`, change visibility in the layers menu, merge layer with the one below it (layer menu), selection to new layer `ctrl + shift + l > ctrl + shift + n` 
 - masking -- basically just make new layers and draw masks for the image with the many drawing tools. This + selection tool allows you to make any boolean operation between the layers