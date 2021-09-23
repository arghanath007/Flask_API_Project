from app.main import db

def save_changes(object,table_name):
    
    try:
        db.session.add(object)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return_object={
            'message': f'Error in {table_name}',
            'error': str(e),
        }
        return return_object,500