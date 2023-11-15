class Person:
    """
    사람을 나타내는 클래스입니다.

    속성:
    - id: 사람의 식별 번호입니다.
    - title: 사람의 직함이나 이름입니다.
    """

    def __init__(self, person_id, title):
        """
        사람 클래스의 초기화 함수입니다.

        Args:
        - person_id: 사람의 고유한 식별 번호입니다.
        - title: 사람의 이름이나 직함입니다.
        """
        self.id = person_id
        self.title = title

    def printInfo(self):
        """
        사람 정보를 출력하는 메서드입니다.
        """
        print(f"ID: {self.id}, Title: {self.title}")


class Manager(Person):
    """
    매니저를 나타내는 클래스입니다. 사람 클래스를 상속받습니다.

    추가된 속성:
    - skill: 매니저의 보유 기술입니다.
    """

    def __init__(self, person_id, title, skill):
        """
        매니저 클래스의 초기화 함수입니다.

        Args:
        - person_id: 매니저의 고유한 식별 번호입니다.
        - title: 매니저의 이름이나 직함입니다.
        - skill: 매니저의 보유 기술입니다.
        """
        super().__init__(person_id, title)
        self.skill = skill

    def printInfo(self):
        """
        매니저 정보를 출력하는 메서드입니다.
        """
        super().printInfo()
        print(f"Skill: {self.skill}")


class Employee(Person):
    """
    직원을 나타내는 클래스입니다. 사람 클래스를 상속받습니다.

    추가된 속성:
    - role: 직원의 역할이나 직무입니다.
    """

    def __init__(self, person_id, title, role):
        """
        직원 클래스의 초기화 함수입니다.

        Args:
        - person_id: 직원의 고유한 식별 번호입니다.
        - title: 직원의 이름이나 직함입니다.
        - role: 직원의 역할이나 직무입니다.
        """
        super().__init__(person_id, title)
        self.role = role


# 샘플 테스트 케이스
# 인스턴스를 생성하고 기능을 테스트합니다.

# Test 1 - Person 인스턴스 생성 및 정보 출력
person = Person(1, "John Doe")
person.printInfo()

# Test 2 - Manager 인스턴스 생성 및 정보 출력
manager = Manager(2, "Jane Smith", "리더십")
manager.printInfo()

# Test 3 - Employee 인스턴스 생성 및 정보 출력
employee = Employee(3, "Alice Johnson", "개발자")
employee.printInfo()

# ... (나머지 샘플 테스트 케이스들도 이어집니다)
p1 = Person(100, "개발자")
p1.printInfo()