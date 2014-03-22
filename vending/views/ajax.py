import json

from vending.views import selects

def handle_update(request):
    
    if "caliber" == request.GET['update']:
        #print "updating caliber"
        return json.dumps( selects.caliber_changed(request) )

    elif "company" == request.GET['update']:
        #print "updating company"
        return json.dumps( selects.company_changed(request) )

    elif "purpose" == request.GET['update']:
        #print "updating purpose"
        return json.dumps( selects.purpose_changed(request) )

    elif "weapon" == request.GET['update']:
        #print "updating weapon"
        return json.dumps( selects.weapon_changed(request) )

    else:
        print "interesting ..."
        return json.dumps( {'action' : 'success','message':'hrrrmmm',} )

