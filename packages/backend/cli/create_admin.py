from getpass import getpass

from backend.core.password import hash_password
from backend.db.session import get_session
from backend.models.user import User
from backend.repositories.users import get_user_by_emp_id
from sqlalchemy.exc import IntegrityError


def create_admin() -> None:
  emp_id = input('사번: ').strip()
  name = input('이름: ').strip()

  if not 1 <= len(emp_id) <= 30 or not 1 <= len(name) <= 100:
    print('사번은 1~30자, 이름은 1~100자여야 합니다.')
    return

  password = getpass('비밀번호: ')
  if not 12 <= len(password) <= 30:
    print('비밀번호는 12~30자여야 합니다.')
    return

  if password != getpass('비밀번호 확인: '):
    print('비밀번호가 일치하지 않습니다.')
    return

  try:
    with get_session() as session:
      if get_user_by_emp_id(session, emp_id) is not None:
        print('이미 등록된 사번입니다.')
        return

      user = User(emp_id=emp_id, name=name, password_hash=hash_password(password), department=None, role='system_admin')
      session.add(user)
  except IntegrityError:
    print('생성에 실패했습니다. 사번 중복 또는 DB 제약을 확인하세요.')
    return

  print('시스템 관리자를 생성했습니다.')


if __name__ == '__main__':
  create_admin()

## 윤수아 짱
