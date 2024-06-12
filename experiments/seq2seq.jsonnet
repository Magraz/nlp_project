local common_parameters = import 'common_seq2seq.libjsonnet';

std.mergePatch(common_parameters, {
  dataset_reader: {
    source_token_indexers: {
      source_tokens: {
        type: 'single_id',
        namespace: 'source_tokens',
      },
    },
  },
  model: {
    "use_bleu": true,
    source_embedder: {
      token_embedders: {
        source_tokens: {
          type: 'embedding',
          vocab_namespace: 'source_tokens',
          embedding_dim: 100,
          trainable: true,
        },
      },
    },
  },
  data_loader: {
    batch_sampler: {
      batch_size: 16,
    },
  },
  trainer: {

  },
})