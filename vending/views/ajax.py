import json

from vending.views import selects

def handle_update(request):
    
    if "caliber" == request.GET['update']:
        #print "updating caliber"
        return json.dumps( selects.caliber_changed(request) )

    elif "manufacturer" == request.GET['update']:
        #print "updating company"
        return json.dumps( selects.manufacturer_changed(request) )

    elif "bullet" == request.GET['update']:
        #print "updating purpose"
        return json.dumps( selects.bullet_changed(request) )

    elif "material" == request.GET['update']:
        #print "updating weapon"
        return json.dumps( selects.material_changed(request) )

    else:
        print "interesting ..."
        return json.dumps( {'action' : 'success','message':'hrrrmmm',} )

