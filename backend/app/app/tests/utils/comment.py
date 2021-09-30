# OpenPantheon: the pantheon for Education
# Copyright (C) 2021 CRI
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.comment import CommentFull
from app.tests.utils.utils import random_lower_string
from app.tests.utils.user import create_random_user
from app.tests.utils.personality import create_random_personality
import random

def create_random_comment(db: Session) -> models.Comment:
	personality = create_random_personality(db)
	user = create_random_user(db)
	text = random_lower_string()
	fluff = ''
	num = random.randint(0, 10)
	for i in range(num):
		if i != 0:
			fluff += '~'
		fluff += random_lower_string() + '|' + 'http://google.fr'
	comment_in = CommentFull(id=random.randint(0, 10000000), author_id=user.id, personality_id=personality.id, text=text, fluff=fluff)
	return crud.comment.create_new_comment(db=db, obj_in=comment_in)
