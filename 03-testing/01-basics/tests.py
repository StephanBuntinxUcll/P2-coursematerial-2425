


from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))


def test_overlapping_intervals2():   
    assert overlapping_intervals((1,5),(5,8))
    assert not overlapping_intervals((0,4),(5,8))

def test_overlapping_intervals3():   
    assert overlapping_intervals((0,4),(0,4))
    assert not overlapping_intervals((0,4),(4,0))

def test_overlapping_intervals4():   
    assert overlapping_intervals((1,2),(0,1))
    assert not overlapping_intervals((6,10),(10,6))


def test_overlapping_intervals5():   
    assert not overlapping_intervals((6,5),(5,6))