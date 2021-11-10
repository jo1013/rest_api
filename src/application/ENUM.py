from enum import Enum


class transform(Enum):
    child = '어린이사고'
    bicycle = '자전거사고'
    dawn = '야간사고'
    old = '노인사고'
    pedestrian = '보행자사고'
    ##################
    code = '법정동코드'
    cases = '사고건수'
    cases_ratio = '사고건수 구성비'
    die = '사망자수'
    dieratio = '사망자수 구성비'
    fatality = '치사율'
    lnjured = '부상자수'
    lnjuredratio = '부상자수 구성비'