{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "users =[\n",
    "    { \"id\":0, \"name\": \"Hero\" },\n",
    "    { \"id\":1, \"name\": \"Dunn\" },\n",
    "    { \"id\":2, \"name\": \"Sue\" },\n",
    "    { \"id\":3, \"name\": \"Chi\" },\n",
    "    { \"id\":4, \"name\": \"Thor\" },\n",
    "    { \"id\":5, \"name\": \"Clive\" },\n",
    "    { \"id\":6, \"name\": \"Hicks\" },\n",
    "    { \"id\":7, \"name\": \"Devin\" },\n",
    "    { \"id\":8, \"name\": \"Kate\" },\n",
    "    { \"id\":9, \"name\": \"Klein\" }    \n",
    "]\n",
    "\n",
    "friendship = [\n",
    "    (0, 1),\n",
    "    (0, 2),\n",
    "    (1, 2),\n",
    "    (1, 3),\n",
    "    (2, 3),\n",
    "    (3, 4),\n",
    "    (4, 5),\n",
    "    (5, 6),\n",
    "    (6, 7),\n",
    "    (6, 8),\n",
    "    (7, 8),\n",
    "    (8, 9)\n",
    "]\n",
    "\n",
    "def search_id(user):\n",
    "    for u in users:\n",
    "        if u[\"name\"] == user:\n",
    "            return u[\"id\"]\n",
    "        \n",
    "def num_friends(user):\n",
    "    id = search_id(user)\n",
    "    count = 0\n",
    "    for i in friendship:\n",
    "        temp = i.count(id)\n",
    "        count = count + temp\n",
    "    return count\n",
    "    \n",
    "#print(num_friends(\"Hero\"))\n",
    "\n",
    "\n",
    "def sort_by_num_friends():\n",
    "    list = []\n",
    "    for user in users:\n",
    "        dict = {}\n",
    "        dict[\"name\"] = user[\"name\"]\n",
    "        dict[\"num_friends\"] = num_friends(user[\"name\"])\n",
    "        list.append(dict)\n",
    "    list = sorted(list, key=lambda k:k['num_friends'], reverse=True)\n",
    "    return list\n",
    "    \n",
    "#print(sort_by_num_friends())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
