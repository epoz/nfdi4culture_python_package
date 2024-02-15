# NFDI4Culture

This is a placeholder for the Python tools being developed to manage the infrastructure of [NFDI4Culture](https://nfdi4culture.de/)

Example:

```python
from nfdi4culture import cto
from lidolator import from_file

item = cto.Item()

item.datafeed = "https://nfdi4culture.de/id/E5320"
# Or should we have cto.DataFeed("https://nfdi4culture.de/id/E5320") and the rest happens from there?
# either of the above will set things like .publisher on the Item too.
# and create the relevant schema.DataFeedItem and schema.DataFeed triples?

item.sourcefile = "http://foo.com/bar/baz.oai-pmh?id=123456"

# the update method expects a dict with key-value mappings
# the cto.Item objet knows how to map a key and value to the relevant fields.
# How do we specify this field mapping?
# And do we split it into a NamedNode/Literal difference?
item.update(from_file(filepath))

item.ntriples()
# or
item.turtle()
```
