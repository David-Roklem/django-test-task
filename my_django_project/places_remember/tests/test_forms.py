import pytest
from django import forms
from places_remember.forms import MemoryForm


@pytest.fixture(scope='function')
def memory_form():
    data = {
        'title': 'Test Memory',
        'comment': 'This is a test comment'
    }
    yield MemoryForm(data=data)


def test_memoryform_valid(memory_form):
    assert memory_form.is_valid() is True


def test_memoryform_invalid_title(memory_form):
    print(memory_form.fields)
    memory_form.data['title'] = ''
    assert memory_form.is_valid() is False


def test_memoryform_fields(memory_form):
    assert isinstance(memory_form.fields['title'], forms.CharField)
    assert isinstance(memory_form.fields['comment'], forms.CharField)
