from segment.campain_push.helper import insert_user


def write_his_data(event):
    msisdn = event.get('msisdn', None)
    subs_package = event.get('package', None)
    if not msisdn or not subs_package:
        insert_user(msisdn, subs_package)
    return event