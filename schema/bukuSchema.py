from marshmallow import Schema, fields, validate

class BukuSchema(Schema):
    id = fields.String(dump_only=True)
    judul_buku = fields.String(required=True)
    kategori_buku = fields.String(required=True)
    penerbit = fields.String(required=True)
    pengarang = fields.String(required=True)
    class Meta:
            strict = True