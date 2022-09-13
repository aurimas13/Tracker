import glob
import unittest
import sys
import os
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
from app.models import Story, Task, Developer, TaskActualTimes



def test_new_story():
    """
    GIVEN a Story model
    WHEN a new Story is created
    THEN check the name, status, description, estimated_time
    """
    story = Story('John', True, 'I\'m awesome', 11)
    assert story.story_name == 'John'
    assert story.status != False
    assert story.description == 'I\'m awesome'
    assert story.estimated_time == 11


def test_new_task():
    """
    GIVEN a Task model
    WHEN a new Task is created
    THEN check story id, name, status, description, estimated_time,. developer id, iteration
    """
    task = Task(1, 'Emma', True, 'She\'s awesome', 15, 1, 'Story #1')
    assert task.story_id == 1
    assert task.task_name == 'Emma'
    assert task.status != False
    assert task.description == 'She\'s awesome'
    assert task.estimated_time == 15
    assert task.developer_id == 1
    assert task.iteration == "Story #1"


def test_new_actual_task_time():
    """
    GIVEN a TaskActualTimes model
    WHEN a new TaskActualTimes is created
    THEN check task id, actual_time
    """
    task_actual = TaskActualTimes(1, 7)

    assert task_actual.task_id == 1
    assert task_actual.actual_time == 7


def test_new_developer():
    """
    GIVEN a Developer model
    WHEN a new Developer is created
    THEN check name
    """
    developer = Developer('Rocky')

    assert developer.name == 'Rocky'

if __name__ == '__main__':
    unittest.main()