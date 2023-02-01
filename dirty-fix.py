with open("./node_modules/mirador/dist/es/src/lib/MiradorCanvas.js") as f:
    text = f.read()

with open("./node_modules/mirador/dist/es/src/lib/MiradorCanvas.js", "w") as f:
    f.write(text.replace(
        """var fragmentMatch = (on || target).match(/xywh=(.*)$/);""",
        """if(!target && !on) {
        console.log(resourceAnnotation);
        return undefined;
      }
      var fragmentMatch = (on || target).match(/xywh=(.*)$/);"""
    ))